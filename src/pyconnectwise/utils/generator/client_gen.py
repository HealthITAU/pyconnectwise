import os

from pyconnectwise.utils.fs import save_py_file
from pyconnectwise.utils.generator.templates import (
    automate_client_template,
    manage_client_template,
)


def generate_manage_client(client_output_path, endpoints):  # noqa: ANN001, ANN201
    imports = [
        f"from pyconnectwise.endpoints.manage.{endpoint} import {endpoint}"
        for endpoint in endpoints
    ]
    endpoint_registrations = [
        {"field_name": endpoint.replace("Endpoint", "").lower(), "class_name": endpoint}
        for endpoint in endpoints
    ]
    client_code = manage_client_template.render(
        imports=imports, endpoints=endpoint_registrations
    )
    save_py_file(
        os.path.join(client_output_path, "manage_client.py"),  # noqa: PTH118
        client_code,
    )


def generate_automate_client(client_output_path, endpoints):  # noqa: ANN001, ANN201
    imports = [
        f"from pyconnectwise.endpoints.automate.{endpoint} import {endpoint}"
        for endpoint in endpoints
    ]
    endpoint_registrations = [
        {"field_name": endpoint.replace("Endpoint", "").lower(), "class_name": endpoint}
        for endpoint in endpoints
    ]
    client_code = automate_client_template.render(
        imports=imports, endpoints=endpoint_registrations
    )
    save_py_file(
        os.path.join(client_output_path, "automate_client.py"),  # noqa: PTH118
        client_code,
    )
