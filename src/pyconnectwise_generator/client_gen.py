import os
from typing import Literal

from pyconnectwise_generator.templates import (
    automate_client_template,
    manage_client_template,
)
from pyconnectwise_generator.utils.fs import save_py_file


def create_null_client(client_output_path: str, client_type: Literal["automate", "manage"]) -> None:
    """Create an empty client to avoid import errors in case the last generation didn't work right"""
    client_code = f"""class ConnectWise{client_type[0].upper()}{client_type[1:]}APIClient:
        pass
    """

    save_py_file(
        os.path.join(client_output_path, f"{client_type}_client.py"),  # noqa: PTH118
        client_code,
    )


def generate_manage_client(client_output_path: str, endpoints: list[str]) -> None:
    imports = [f"from pyconnectwise.endpoints.manage.{endpoint} import {endpoint}" for endpoint in endpoints]
    endpoint_registrations = [
        {"field_name": endpoint.replace("Endpoint", "").lower(), "class_name": endpoint} for endpoint in endpoints
    ]
    client_code = manage_client_template.render(imports=imports, endpoints=endpoint_registrations)
    save_py_file(
        os.path.join(client_output_path, "manage_client.py"),  # noqa: PTH118
        client_code,
    )


def generate_automate_client(client_output_path: str, endpoints: list[str]) -> None:
    imports = [f"from pyconnectwise.endpoints.automate.{endpoint} import {endpoint}" for endpoint in endpoints]
    endpoint_registrations = [
        {"field_name": endpoint.replace("Endpoint", "").lower(), "class_name": endpoint} for endpoint in endpoints
    ]
    client_code = automate_client_template.render(imports=imports, endpoints=endpoint_registrations)
    save_py_file(
        os.path.join(client_output_path, "automate_client.py"),  # noqa: PTH118
        client_code,
    )
