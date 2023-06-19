from pyconnectwise.utils.generator.templates import manage_client_template
from pyconnectwise.utils.fs import save_py_file
import os

def generate_client(client_output_path, endpoints):
    imports = [f"from pyconnectwise.endpoints.manage.{endpoint} import {endpoint}" for endpoint in endpoints]
    endpoint_registrations = [{'field_name': endpoint.replace('Endpoint', '').lower(), 'class_name': endpoint} for endpoint in endpoints]
    client_code = manage_client_template.render(imports=imports, endpoints=endpoint_registrations)
    save_py_file(os.path.join(client_output_path, 'manage_client.py'), client_code)