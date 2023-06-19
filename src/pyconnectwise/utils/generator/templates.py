from jinja2 import Template

endpoint_template = Template(
"""from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
{%- if additional_imports is defined %}
{%- for additional_import in additional_imports %}
{{ additional_import }}
{%- endfor %}
{%- endif %}

class {{ endpoint_class }}(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{{ endpoint_path }}", parent_endpoint=parent_endpoint)
        {% if child_endpoints is defined %}
        {%- for child_endpoint in child_endpoints %}
        self.{{ child_endpoint.field_name }} = self.register_child_endpoint(
            {{ child_endpoint.class_name }}(client, parent_endpoint=self)
        )
        {%- endfor %}
        {%- endif %}
    
    {% if has_id_child %}
    def id(self, id: int) -> {{ id_child_endpoint_class }}:
        \"""
        Sets the ID for this endpoint and returns an initialized {{ id_child_endpoint_class }} object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            {{ id_child_endpoint_class }}: The initialized {{ id_child_endpoint_class }} object.
        \"""
        child = {{ id_child_endpoint_class }}(self.client, parent_endpoint=self)
        child._id = id
        return child
    {% endif %}

    {%- if pagination_model_class is not none %}
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[{{ pagination_model_class }}]:
        \"""
        Performs a GET request against the {{ raw_path }} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[{{ pagination_model_class }}]: The initialized PaginatedResponse object.
        \"""
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            {{ pagination_model_class }},
            self,
            page_size,
        )
    {% endif %}

    {%- for operation in operations %}
    def {{ operation.name }}(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> {{ operation.return_type }}:
        \"""
        Performs a {{ operation.name.upper() }} request against the {{ raw_path }} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            {{ operation.return_type }}: The parsed response data.
        \"""
        {%- if operation.returns_single %}
        return self._parse_one({{operation.return_class}}, super().make_request("{{ operation.name.upper() }}", params=params).json())
        {% else %}
        return self._parse_many({{operation.return_class}}, super().make_request("{{ operation.name.upper() }}", params=params).json())
        {% endif %}
    {%- endfor %}
"""
)

top_level_endpoint_template = Template(
"""from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
{%- if additional_imports is defined %}
{%- for additional_import in additional_imports %}
{{ additional_import }}
{%- endfor %}
{%- endif %}

class {{ endpoint_class }}(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "{{ endpoint_path }}")
        {% if child_endpoints is defined %}
        {%- for child_endpoint in child_endpoints %}
        self.{{ child_endpoint.field_name }} = self.register_child_endpoint(
            {{ child_endpoint.class_name }}(client, parent_endpoint=self)
        )
        {%- endfor %}
        {%- endif %}
"""
)

model_template = Template(
"""from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

{%- if mod_enums is defined %}
{%- for mod_enum in mod_enums %}
class {{ mod_enum.e_name }}(str, Enum):
    {%- for enum_value in mod_enum.fields %}
    {{ enum_value.v_name }} = '{{ enum_value.v_value }}'
    {%- endfor %}

{%- endfor %}
{%- endif %}

class {{ model_class }}(ConnectWiseModel):
    {%- for field in fields %}
    {{ field.name }}: {{ field.type }}
    {%- endfor %}

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True
"""
)

manage_client_template = Template(
"""import base64
import requests
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class ConnectWiseManageAPIClient:
    \"""
    ConnectWise Manage API client. Handles the connection to the ConnectWise Manage API
    and the configuration of all the available endpoints.
    \"""
    def __init__(
        self,
        company_name: str,
        manage_url: str,
        client_id: str,
        public_key: str,
        private_key: str,
        codebase: str | None = None,
    ):
        \"""
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            company_name (str): Name of your company.
            manage_url (str): URL of your ConnectWise Manage instance.
            client_id (str): Your ConnectWise Manage API Client ID.
            public_key (str): Your ConnectWise Manage API Public key.
            private_key (str): Your ConnectWise Manage API Private key.
            codebase (str, optional): Your ConnectWise Manage Codebase. If not provided, it will be fetched from the API. Defaults to None.
        \"""
        self.client_id = client_id
        self.company_name = company_name
        self.manage_url = manage_url
        self.public_key = public_key
        self.private_key = private_key
        
        # Retrieve codebase from the API if not provided
        if not codebase:
            codebase_request = self.__try_get_codebase_from_api(
                manage_url=manage_url,
                company_name=company_name,
                headers=self.get_headers(),
            )

            if codebase_request is None:
                # we need to except here
                raise Exception("Could not retrieve codebase from API.")
            self.codebase = codebase_request
            

        # Initializing endpoints
        {%- for endpoint in endpoints %}
        self.{{ endpoint.field_name }} = {{ endpoint.class_name }}(self)
        {%- endfor %}

    def get_url(self) -> str:
        \"""
        Generates and returns the URL for the ConnectWise Manage API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        \"""
        return f"https://{self.manage_url}/{self.codebase.strip('/')}/apis/3.0"

    def __try_get_codebase_from_api(self, manage_url: str, company_name: str, headers: dict[str, str]) -> str | None:
        \"""
        Tries to retrieve the codebase from the API using the provided company url, company name and headers.

        Parameters:
            company_url (str): URL of the company.
            company_name (str): Name of the company.
            headers (dict[str, str]): Headers to be sent in the request.

        Returns:
            str: Codebase string or None if an error occurs.
        \"""
        result = ""
        try:
            url = f"https://{manage_url}/login/companyinfo/{company_name}"
            result = (
                requests.request("GET", url, headers=headers).json().get("Codebase")
            )
        except:
            result = None
        return result

    def __get_auth_string(self) -> str:
        \"""
        Creates and returns the base64 encoded authorization string required for API requests.

        Returns:
            str: Base64 encoded authorization string.
        \"""
        return "Basic " + base64.b64encode(
            bytes(
                f"{self.company_name}+{self.public_key}:{self.private_key}",
                encoding="utf8",
            )
        ).decode("ascii")

    def get_headers(self) -> dict[str, str]:
        \"""
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        \"""
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self.__get_auth_string(),
        }
        return headers

"""
)

automate_client_template = Template(
"""import base64
import requests
from datetime import datetime
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class ConnectWiseAutomateAPIClient:
    \"""
    ConnectWise Automate API client. Handles the connection to the ConnectWise Automate API
    and the configuration of all the available endpoints.
    \"""
    def __init__(
        self,
        automate_url: str,
        client_id: str,
        username: str,
        password: str,
    ):
        \"""
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            automate_url (str): URL of your ConnectWise Automate instance.
            client_id (str): Your ConnectWise Automate API Client ID.
            username (str): Your ConnectWise Automate API username.
            password (str): Your ConnectWise Automate API password.
        \"""
        self.client_id = client_id
        self.automate_url = automate_url
        self.username = username
        self.password = password
        self.token_expiry_time: datetime = datetime.now().isoformat()

        # Grab first access token
        self.access_token: str = __get_access_token()
                
        # Initializing endpoints
        {%- for endpoint in endpoints %}
        self.{{ endpoint.field_name }} = {{ endpoint.class_name }}(self)
        {%- endfor %}

    def get_url(self) -> str:
        \"""
        Generates and returns the URL for the ConnectWise Automate API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        \"""
        return f"https://{self.automate_url}/cwa"

    def __get_access_token() -> str:
        token = ""
        try:
            result

    def get_headers(self) -> dict[str, str]:
        \"""
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        \"""
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": f"Bearer {self.access_token}",
        }
        return headers

"""
)
