# endpoint_gen.py in src/pyconnectwise/utils/generator
import os
from pyconnectwise.utils.fs import save_py_file
from pyconnectwise.utils.generator.templates import (
    endpoint_template,
)
from pyconnectwise.utils.generator.path_formatting import (
    format_endpoint_path,
    get_endpoint_class_name_from_path,
    normalize_path_parameters,
)
from pyconnectwise.utils.naming import to_snake_case, ensure_not_reserved


def generate_endpoint(
    endpoint_output_directory: str,
    model_output_directory: str,
    path: str,
    path_info: dict,
    relationships: dict,
):
    print(path)
    formatted_path = format_endpoint_path(path)
    endpoint_class_name = get_endpoint_class_name_from_path(formatted_path)
    model_class_name = endpoint_class_name.replace("Endpoint", "Model")
    model_module_name = model_class_name.lower()
    endpoint_import_directory = endpoint_output_directory.split("/")[-1]
    model_import_directory = model_output_directory.split("/")[-1]

    operations = list(path_info.keys())

    child_endpoints = list(
        set(format_endpoint_path(child)
            for child in relationships.get(path, []))
    )

    print(f"Generating {endpoint_class_name}")

    id_child_endpoint_class_name = None
    has_id_child = False
    additional_imports = []
    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        if not child_endpoint:
            continue

        if "Id" in child_endpoint:
            id_child_endpoint_class_name = endpoint_class_name.replace(
                "Endpoint", f"IdEndpoint"
            )
            if endpoint_class_name == id_child_endpoint_class_name:
                continue

            additional_imports.append(
                f"from pyconnectwise.endpoints.{endpoint_import_directory}.{id_child_endpoint_class_name} import {id_child_endpoint_class_name}"
            )
            has_id_child = True
        else:
            child_endpoint_path = child_endpoint
            child_endpoint_class_name = get_endpoint_class_name_from_path(
                child_endpoint
            )
            if endpoint_class_name == child_endpoint_class_name:
                continue

            child_endpoint_definitions.append(
                {
                    "field_name": ensure_not_reserved(
                        to_snake_case(child_endpoint.split("/")[-1])
                    ),
                    "class_name": endpoint_class_name.replace(
                        "Endpoint", child_endpoint_class_name
                    ),
                    "path": child_endpoint_path.split("/")[-1],
                }
            )
            additional_imports.append(
                f"from pyconnectwise.endpoints.{endpoint_import_directory}.{endpoint_class_name.replace('Endpoint', child_endpoint_class_name)} import {endpoint_class_name.replace('Endpoint', child_endpoint_class_name)}"
            )

    imported_models = []
    op_definitions = []
    pagination_model_class = None
    for operation in operations:
        print(f"        Processing OP: {operation}")
        if (
            path_info.get(operation) is None
            or path_info[operation].get("responses") is None
        ):
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
                op_definitions.append(
                    {
                        "name": operation,
                        "void": True
                    }
                )
            else:
                resp_content = response.get("content")
                schema_object = resp_content.get(
                    list(resp_content)[0]).get("schema")
                schema_ref = None
                is_array = False

                if schema_object.get("type") == "array":
                    is_array = True
                    schema_ref = schema_object.get("items").get("$ref")
                elif (
                    schema_object.get("type") == "object"
                    and schema_object.get("additionalProperties") is not None
                    and schema_object.get("$ref") is not None
                ):
                    schema_ref = schema_object.get(
                        "additionalProperties").get("$ref")
                else:
                    schema_ref = schema_object.get("$ref")

                if schema_ref:
                    model_name = schema_ref.split("/")[-1]
                    split = model_name.split(".")
                    if len(split) >= 2:
                        model_name = split[0] + split[-1]
                    else:
                        model_name = "".join(model_name.split("."))
                    return_type = model_name

                    for param in operation_params:
                        param_name = param.get("name")
                        if param_name is not None:
                            if "page" in param_name:
                                pagination_model_class = model_name

                    if is_array:
                        return_type = f"list[{model_name}]"

                    if model_name not in imported_models:
                        additional_imports.append(
                            f"from pyconnectwise.models.{model_import_directory} import {model_name}"
                        )
                        imported_models.append(model_name)

                    op_definitions.append(
                        {
                            "name": operation,
                            "return_type": return_type,
                            "return_class": model_name,
                            "returns_single": not is_array,
                        }
                    )

    endpoint_code = endpoint_template.render(
        endpoint_class=endpoint_class_name,
        model_class=model_class_name,
        model_module=model_module_name,
        pagination_model_class=pagination_model_class,
        endpoint_path=normalize_path_parameters(
            path.split("/")[-1]).rstrip("/"),
        operations=op_definitions,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        id_child_endpoint_class=id_child_endpoint_class_name,
        has_id_child=has_id_child,
        raw_path=path,
    )

    save_py_file(
        os.path.join(endpoint_output_directory,
                     endpoint_class_name), endpoint_code
    )
    return endpoint_class_name
