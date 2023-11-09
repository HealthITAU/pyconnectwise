import typer

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
    client_output_path: str = "src/pyconnectwise/clients/manage_client.py",
) -> None:
    schema = load_schema(schema_path)
    generate_manage(endpoint_output_path, model_output_path, client_output_path, schema)


@app.command()
def generate_automate_code(  # noqa: ANN201
    schema_folder_path: str,
    *,
    endpoint_output_path: str = "src/pyconnectwise/endpoints/automate",
    model_output_path: str = "src/pyconnectwise/models/automate",
    client_output_path: str = "src/pyconnectwise/clients/automate_client.py",
):
    schema = merge_automate_specs(schema_folder_path)
    # schema = load_schema(schema_path)
    #
    generate_automate(
        endpoint_output_path, model_output_path, client_output_path, schema
    )
    pass


app()
