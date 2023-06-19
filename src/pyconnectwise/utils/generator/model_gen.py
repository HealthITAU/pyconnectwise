### THIS CODE IS NOT INTENDED FOR REGULAR USE
### It's used to generate Endpoints from the schema
### It's messy and not very readable
### Works as is but proceed at your own risk.

from pyconnectwise.utils.generator.templates import model_template
from pyconnectwise.utils.naming import to_snake_case
from pyconnectwise.utils.fs import save_py_file
import os


def generate_model(
    file_output_directory: str, model_name: str, model_schema: dict, models: dict
):
    print(f"            Attempting to generate model: {model_name}")

    cleaned_name = None

    if "." in model_name:
        cleaned_name = model_name.split(".")[-1] + "Model"
    else:
        cleaned_name = model_name + "Model"

    model_class_name = cleaned_name

    if os.path.exists(os.path.join(file_output_directory, model_class_name)):
        print(f"            Model already exists: {model_class_name}")
        return model_class_name

    properties = model_schema.get("properties")
    fields = []
    imports = []
    enums = []
    has_imported_enum = False

    def convert_type_name(input_type: str, input_format: str | None = None) -> str:
        match input_type:
            case "string":
                if input_format == "date-time":
                    return "datetime"
                return "str"
            case "integer":
                return "int"
            case "boolean":
                return "bool"
            case "double":
                return "float"
            case _:
                return "str"

    print(f"            Iterating model properties")
    if properties is not None:
        for field_name, field_schema in properties.items():
            print(f"                Processing property: {field_name}")
            if field_schema.get("$ref") is not None:
                # nested model
                nested_schema = field_schema.get("$ref")
                is_array = False
                if field_schema.get("type") == "array":
                    is_array = True
                nested_model_name = nested_schema.split("/")[-1]
                nested_model_schema = models[nested_model_name]
                nested_class_name = generate_model(
                    file_output_directory,
                    nested_model_name,
                    nested_model_schema,
                    models,
                )
                field_type = nested_class_name
                if is_array:
                    field_type = f"list[{field_type}]"

                ### Optional fields aren't labelled as such in CWM's schema
                ### As a consequence of this, everything is <type> | None until I think of a better solution that doesn't involve me manually editing the schema
                #field_type += " | None"

                fields.append(
                    {
                        "name": to_snake_case(field_name),
                        "type": field_type,
                    }
                )

                if model_class_name == f"{nested_model_name}Model":
                    print(
                        f"                Skipping import for {nested_model_name}Model as its ourself <{model_class_name}>"
                    )
                else:
                    imports.append(
                        f"from pyconnectwise.models.manage.{nested_model_name}Model import {nested_model_name}Model"
                    )
            else:
                schema_type = field_schema.get("type")
                schema_format = field_schema.get("format")
                field_type = None
                if field_schema.get("enum") is not None:
                    enum_values = field_schema.get("enum")
                    enum_name = field_name[:1].upper() + field_name[1:]

                    if not has_imported_enum:
                        imports.append("from enum import Enum")
                        has_imported_enum = True

                    pp_values = []
                    for value in enum_values:
                        if (
                            value.lower() == "none"
                            or value.lower() == "true"
                            or value.lower() == "false"
                        ):
                            pp_values.append(value.upper())
                        else:
                            pp_values.append(value)

                    if enum_name.lower() == "type":
                        enum_name = f"{model_class_name}Type"

                    enums.append(
                        {
                            "e_name": enum_name,
                            "fields": [
                                {
                                    "v_name": value,
                                    "v_value": value,
                                    "v_type": convert_type_name(schema_type, schema_format),
                                }
                                for value in pp_values
                            ],
                        }
                    )

                    field_type = enum_name
                else:
                    if schema_type == "array":
                        item_type = field_schema.get("items").get("type")
                        item_format = field_schema.get("items").get("format")
                        if item_type is None:
                            if field_schema.get("items").get("$ref") is not None:
                                nested_schema = field_schema.get("items").get("$ref")
                                nested_model_name = nested_schema.split("/")[-1]
                                nested_model_schema = models[nested_model_name]
                                nested_class_name = generate_model(
                                    file_output_directory,
                                    nested_model_name,
                                    nested_model_schema,
                                    models,
                                )
                                field_type = f"list[{nested_class_name}]"
                                imports.append(
                                    f"from pyconnectwise.models.manage.{nested_class_name} import {nested_class_name}"
                                )
                            else:
                                field_type = "list[Any]"
                        else:
                            field_type = f"list[{convert_type_name(item_type, item_format)}]"
                    elif schema_type == "object":
                        props = field_schema.get("additionalProperties")
                        if props is None:
                            item_type = "Any"
                            field_type = f"Any"
                        else:
                            item_type = props.get("type")
                            field_type = f"dict[str, {convert_type_name(item_type)}]"
                    elif schema_type == "number":
                        format = field_schema.get("format")
                        field_type = convert_type_name(format)
                    else:
                        field_type = convert_type_name(schema_type)

                ### Optional fields aren't labelled as such in CWM's schema
                ### As a consequence of this, everything is <type> | None until I think of a better solution that doesn't involve me manually editing the schema
                #field_type += " | None"

                fields.append(
                    {
                        "name": to_snake_case(field_name),
                        "type": field_type,
                    }
                )

    model_code = model_template.render(
        mod_enums=enums, model_class=model_class_name, imports=imports, fields=fields
    )

    save_py_file(os.path.join(file_output_directory, model_class_name), model_code)
    return model_class_name