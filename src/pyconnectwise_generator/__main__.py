import logging
from pathlib import Path

import typer

from pyconnectwise_generator.normalize_schema_refs import normalize_json_schema

from .models import generate_models
from .parser import (
    generate_automate,
    generate_manage,
    load_schema,
    merge_automate_specs,
)

app = typer.Typer()


@app.command()
def generate_manage_code(
    schema_path: str,
    *,
    endpoint_output_path: str = "src/pyconnectwise/endpoints/manage",
    model_output_path: str = "src/pyconnectwise/models/manage",
    client_output_path: str = "src/pyconnectwise/clients",
) -> None:
    schema = load_schema(schema_path)
    schema = normalize_json_schema(schema)
    logging.info("Generating models")
    generate_models(schema, Path(model_output_path) / "__init__.py")
    generate_manage(endpoint_output_path, model_output_path, client_output_path, schema)

    print("After generating run `ruff src/pyconnectwise/models/manage --fix --unsafe-fixes`")


@app.command()
def generate_automate_code(  # noqa: ANN201
    schema_folder_path: str,
    *,
    endpoint_output_path: str = "src/pyconnectwise/endpoints/automate",
    model_output_path: str = "src/pyconnectwise/models/automate",
    client_output_path: str = "src/pyconnectwise/clients",
):
    schema = merge_automate_specs(schema_folder_path)
    # schema = load_schema(schema_path)

    # Does this need normalize_json_schema too??
    generate_models(schema, Path(model_output_path) / "__init__.py")
    generate_automate(endpoint_output_path, model_output_path, client_output_path, schema)
    pass

    print("After generating run `ruff src/pyconnectwise/models/automate --fix --unsafe-fixes`")


app()
