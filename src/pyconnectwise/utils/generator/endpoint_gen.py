### THIS CODE IS NOT INTENDED FOR REGULAR USE
### It's used to generate Endpoints from the schema
### It's messy and not very readable
### Works as is but proceed at your own risk.

from pyconnectwise.utils.generator.templates import (
    endpoint_template,
    top_level_endpoint_template,
)
from pyconnectwise.utils.fs import save_py_file
from pyconnectwise.utils.naming import to_title_case_preserve_case
from pyconnectwise.utils.generator.model_gen import generate_model
import os
import re

def format_endpoint_path(path: str) -> str:
    return re.sub("{id}|{parentId}|{grandparentId}|{reportName}|{externalId}", "Id", path).rstrip("/")

def generate_endpoint(
    endpoint_output_directory: str,
    model_output_directory: str,
    path: str,
    path_info: dict,
    relationships: dict,
    models: dict,
):
    formatted_path = format_endpoint_path(path)
    endpoint_class_name = "".join(to_title_case_preserve_case(word) for word in formatted_path.split("/")) + "Endpoint"
    model_class_name = endpoint_class_name.replace("Endpoint", "Model")
    model_module_name = model_class_name.lower()
    is_top_level_endpoint = False

    top_level_check = formatted_path.lstrip("/").split("/")
    if len(top_level_check) == 1:
        is_top_level_endpoint = True

    operations = list(path_info.keys())

    child_endpoints = relationships.get(formatted_path, [])

    print(f"Generating {endpoint_class_name}")

    id_child_endpoint_class_name = None
    has_id_child = False
    additional_imports = []
    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        if not child_endpoint:
            continue

        if "Id" in child_endpoint:
            id_child_endpoint_class_name = endpoint_class_name.replace("Endpoint", f"IdEndpoint")
            if endpoint_class_name == id_child_endpoint_class_name:
                continue

            additional_imports.append(f"from pyconnectwise.endpoints.manage.{id_child_endpoint_class_name} import {id_child_endpoint_class_name}")
            has_id_child = True
        else:
            child_endpoint_path = child_endpoint
            child_endpoint_class_name = "".join(to_title_case_preserve_case(word) for word in child_endpoint.split("/")) + "Endpoint"
            if endpoint_class_name == child_endpoint_class_name:
                continue

            field_name = None
            name_segments = child_endpoint.split("/")
            if len(name_segments) == 1:
                field_name = name_segments[0]
            else:
                field_name = name_segments[-1]
            child_endpoint_definitions.append(
                {
                    "field_name": field_name,
                    "class_name": endpoint_class_name.replace("Endpoint", child_endpoint_class_name),
                    "path": child_endpoint_path.split("/")[-1],
                }
            )
            additional_imports.append(f"from pyconnectwise.endpoints.manage.{endpoint_class_name.replace('Endpoint', child_endpoint_class_name)} import {endpoint_class_name.replace('Endpoint', child_endpoint_class_name)}")

    imported_models = []
    op_definitions = []
    pagination_model_class = None
    for operation in operations:
        print(f"        Processing OP: {operation}")
        operation_responses = path_info[operation]["responses"]
        operation_params = []

        if path_info[operation].get("parameters") is not None:
            operation_params = path_info[operation]["parameters"]

        for response in operation_responses.values():
            if response.get("content") is None:
                op_definitions.append(
                    {
                        "name": operation,
                        "return_type": "GenericMessageModel",
                        "return_class": "GenericMessageModel",
                        "returns_single": True,
                    }
                )
            else:
                resp_content = response.get("content")
                schema_object = resp_content.get(list(resp_content)[0]).get("schema")
                schema_ref = None
                is_array = False

                if schema_object.get("type") == "array":
                    is_array = True
                    schema_ref = schema_object.get("items").get("$ref")
                elif schema_object.get("type") == "object" and schema_object.get("additionalProperties") is not None and schema_object.get("$ref") is not None:
                    schema_ref = schema_object.get("additionalProperties").get("$ref")
                else:
                    schema_ref = schema_object.get("$ref")
                    
                if schema_ref:
                    model_name = schema_ref.split("/")[-1]
                    model_schema = models[model_name]
                    generated_class_name = generate_model(
                        model_output_directory, model_name, model_schema, models
                    )
                    return_type = generated_class_name
                    return_class = return_type

                    for param in operation_params:
                        param_name = param.get('name')
                        if param_name is not None:
                            if "page" in param_name:
                                pagination_model_class = generated_class_name

                    if is_array:
                        return_type = f"list[{return_type}]"

                    if generated_class_name not in imported_models:
                        additional_imports.append(
                            f"from pyconnectwise.models.manage.{generated_class_name} import {generated_class_name}"
                        )
                        imported_models.append(generated_class_name)

                    op_definitions.append(
                        {
                            "name": operation,
                            "return_type": return_type,
                            "return_class": return_class,
                            "returns_single": not is_array,
                        }
                    )

    endpoint_code = endpoint_template.render(
        endpoint_class=endpoint_class_name,
        model_class=model_class_name,
        model_module=model_module_name,
        pagination_model_class=pagination_model_class,
        endpoint_path=path.split("/")[-1],
        operations=op_definitions,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        id_child_endpoint_class=id_child_endpoint_class_name,
        has_id_child=has_id_child,
        raw_path=path,
    )

    save_py_file(
        os.path.join(endpoint_output_directory, endpoint_class_name), endpoint_code
    )
    return is_top_level_endpoint, endpoint_class_name



def generate_top_level_endpoint(
    endpoint_output_directory: str, path: str, path_info: dict, relationships: dict
):
    formatted_path = format_endpoint_path(path)
    endpoint_class_name = "".join(to_title_case_preserve_case(word) for word in formatted_path.split("/")) + "Endpoint"
    child_endpoints = relationships.get(formatted_path, [])

    print(f"Generating {endpoint_class_name}")

    additional_imports = []
    for child_endpoint in child_endpoints:
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(to_title_case_preserve_case(word) for word in child_endpoint.split("/")) + "Endpoint"
        additional_imports.append(
            f"from pyconnectwise.endpoints.manage.{endpoint_class_name.replace('Endpoint', child_endpoint_class)} import {endpoint_class_name.replace('Endpoint', child_endpoint_class)}"
        )

    child_endpoint_definitions = []
    for child_endpoint in child_endpoints:
        child_endpoint_path = child_endpoint
        child_endpoint_class = "".join(to_title_case_preserve_case(word) for word in child_endpoint.split("/")) + "Endpoint"
        child_endpoint_definitions.append(
            {
                "field_name": child_endpoint.split("/")[-1],
                "class_name": endpoint_class_name.replace("Endpoint", child_endpoint_class),
                "path": child_endpoint_path,
            }
        )

    endpoint_code = top_level_endpoint_template.render(
        endpoint_class=endpoint_class_name,
        child_endpoints=child_endpoint_definitions,
        additional_imports=additional_imports,
        endpoint_path=path.split("/")[-1],
    )

    save_py_file(
        os.path.join(endpoint_output_directory, endpoint_class_name), endpoint_code
    )

    return endpoint_class_name
