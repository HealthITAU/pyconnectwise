# endpoint_gen.py in src/pyconnectwise/utils/generator
import importlib
import logging
import os

from pyconnectwise.utils.naming import ensure_not_reserved, to_snake_case
from pyconnectwise_generator.path_formatting import (
    format_endpoint_path,
    get_endpoint_class_name_from_path,
    normalize_path_parameters,
)
from pyconnectwise_generator.templates import (
    endpoint_template,
)
from pyconnectwise_generator.utils.fs import save_py_file


class ModelNotFoundError(Exception):
    def __init__(self, module_name: str, model_name: str) -> None:
        self.module_name = module_name
        self.model_name = model_name
        super().__init__(f"Model {model_name} not found in module {module_name}")


def generate_endpoint(  # noqa: ANN201, C901
    endpoint_output_directory: str,
    model_output_directory: str,
    path: str,
    path_info: dict,
    relationships: dict,
    *,
    is_manage: bool,
):
    formatted_path = format_endpoint_path(path)
    endpoint_class_name = get_endpoint_class_name_from_path(formatted_path)
    model_class_name = endpoint_class_name.replace("Endpoint", "Model")
    models_module_name = model_class_name.lower()
    endpoint_import_directory = endpoint_output_directory.split("/")[-1]
    model_import_directory = model_output_directory.split("/")[-1]
    models_module_name = f"pyconnectwise.models.{model_import_directory}"

    operations = list(path_info.keys())

    child_endpoints = list({format_endpoint_path(child) for child in relationships.get(path, [])})

    logging.info(f"Generating {endpoint_class_name} from {path}")

    id_child_endpoint_class_name = None
    has_id_child = False
    additional_imports = []
    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        if not child_endpoint:
            continue

        if "Id" in child_endpoint:
            id_child_endpoint_class_name = endpoint_class_name.replace("Endpoint", "IdEndpoint")
            if endpoint_class_name == id_child_endpoint_class_name:
                continue

            additional_imports.append(
                f"from pyconnectwise.endpoints.{endpoint_import_directory}.{id_child_endpoint_class_name} import {id_child_endpoint_class_name}"
            )
            has_id_child = True
        else:
            child_endpoint_path = child_endpoint
            child_endpoint_class_name = get_endpoint_class_name_from_path(child_endpoint)
            if endpoint_class_name == child_endpoint_class_name:
                continue

            child_endpoint_definitions.append(
                {
                    "field_name": ensure_not_reserved(to_snake_case(child_endpoint.split("/")[-1])),
                    "class_name": endpoint_class_name.replace("Endpoint", child_endpoint_class_name),
                    "path": child_endpoint_path.split("/")[-1],
                }
            )
            additional_imports.append(
                f"from pyconnectwise.endpoints.{endpoint_import_directory}.{endpoint_class_name.replace('Endpoint', child_endpoint_class_name)} import {endpoint_class_name.replace('Endpoint', child_endpoint_class_name)}"
            )

    imported_models = []
    op_definitions = []
    interfaces = []
    pagination_model_class = None
    for operation in operations:
        logging.info(f"        Processing OP: {operation}")
        if path_info.get(operation) is None or path_info[operation].get("responses") is None:
            continue
        operation_responses = path_info[operation]["responses"]
        operation_params = []

        if path_info[operation].get("parameters") is not None:
            operation_params = path_info[operation]["parameters"]

        for response in operation_responses.values():
            if response.get("content") is None:
                # op_definitions.append(
                #     {
                #         "name": operation,
                #         "return_type": "GenericMessageModel",
                #         "return_class": "GenericMessageModel",
                #         "returns_single": True,
                #     }
                # )
                op_definitions.append({"name": operation, "void": True})
            else:
                resp_content = response.get("content")
                schema_object = resp_content.get(next(iter(resp_content))).get("schema")
                schema_ref: str | None = None
                is_array: bool = False

                if schema_object.get("type") == "array":
                    is_array = True
                    schema_ref = schema_object.get("items").get("$ref")
                elif (
                    schema_object.get("type") == "object"
                    and schema_object.get("additionalProperties") is not None
                    and schema_object.get("$ref") is not None
                ):
                    schema_ref = schema_object.get("additionalProperties").get("$ref")
                else:
                    schema_ref = schema_object.get("$ref")

                if schema_ref:
                    if not isinstance(schema_ref, str):
                        raise TypeError(f"schema_ref is not a string: {schema_ref}")  # noqa: TRY003
                    model_name = schema_ref.split("/")[-1]

                    model_name_split = model_name.split(".")
                    if len(model_name_split) >= 2:
                        model_name = model_name_split[0] + model_name_split[-1]

                    return_type = model_name

                    for param in operation_params:
                        param_name = param.get("name")
                        if param_name is not None and "page" in param_name:
                            pagination_model_class = model_name

                    if is_array:
                        return_type = f"list[{model_name}]"

                    if model_name not in imported_models:
                        # Check if the model can be be found, otherwise bail so we don't add imports that won't work.
                        if not hasattr(importlib.import_module(models_module_name), model_name):
                            logging.error(f"Class {model_name} does not exist in module {models_module_name}")
                            raise ModelNotFoundError(models_module_name, model_name)

                        additional_imports.append(f"from {models_module_name} import {model_name}")
                        imported_models.append(model_name)

                    op_definitions.append(
                        {
                            "name": operation,
                            "return_type": return_type,
                            "return_class": model_name,
                            "returns_single": not is_array,
                        }
                    )

                    if operation.lower() == "get":
                        interfaces.append(
                            {
                                "class": "IGettable",
                                "return_type": return_type,
                            }
                        )
                    elif operation.lower() == "post":
                        interfaces.append({"class": "IPostable", "return_type": return_type})
                    elif operation.lower() == "patch":
                        interfaces.append({"class": "IPatchable", "return_type": return_type})
                    elif operation.lower() == "put":
                        interfaces.append({"class": "IPuttable", "return_type": return_type})
                    elif operation.lower() == "delete":
                        interfaces.append({"class": "IDeleteable", "return_type": None})

    endpoint_code = endpoint_template.render(
        endpoint_class=endpoint_class_name,
        model_class=model_class_name,
        model_module=models_module_name,
        pagination_model_class=pagination_model_class,
        endpoint_path=normalize_path_parameters(path.split("/")[-1]).rstrip("/"),
        operations=op_definitions,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        id_child_endpoint_class=id_child_endpoint_class_name,
        has_id_child=has_id_child,
        raw_path=path,
        is_manage=is_manage,
        interfaces=interfaces,
    )

    save_py_file(
        os.path.join(endpoint_output_directory, endpoint_class_name),  # noqa: PTH118
        endpoint_code,
    )
    return endpoint_class_name
