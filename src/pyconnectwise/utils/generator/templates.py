from jinja2 import Template

endpoint_template = Template(
    """from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
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
        self.{{ child_endpoint.field_name }} = self._register_child_endpoint(
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
            super()._make_request(
                "GET",
                params=params
            ),
            {{ pagination_model_class }},
            self,
            page,
            page_size,
            params
        )
    {% endif %}

    {%- for operation in operations %}
    def {{ operation.name }}(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> {{ 'None' if operation.void else operation.return_type }}:
        \"""
        Performs a {{ operation.name.upper() }} request against the {{ raw_path }} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        {%- if not operation.void %}
        Returns:
            {{ operation.return_type }}: The parsed response data.
        {%- endif %}
        \"""

        {%- if operation.returns_single %}
        return self._parse_one({{operation.return_class}}, super()._make_request("{{ operation.name.upper() }}", data=data, params=params).json())
        {% elif operation.void %}
        super()._make_request("{{ operation.name.upper() }}", data=data, params=params)
        {% else %}
        return self._parse_many({{operation.return_class}}, super()._make_request("{{ operation.name.upper() }}", data=data, params=params).json())
        {% endif %}
    {%- endfor %}
"""
)

manage_client_template = Template(
    """import base64
from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class ConnectWiseManageAPIClient(ConnectWiseClient):
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
        config: Config = None
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
            config (Config, optional): Optional additional configuration for API interactions
        \"""
        self.client_id: str = client_id
        self.company_name: str = company_name
        self.manage_url: str = manage_url
        self.public_key: str = public_key
        self.private_key: str = private_key
        
        if config:
            self.config = config
        
        # Retrieve codebase from the API if not provided
        if not codebase:
            codebase_request = self._try_get_codebase_from_api(
                manage_url=manage_url,
                company_name=company_name,
                headers=self._get_headers(),
            )

            if codebase_request is None:
                # we need to except here
                raise Exception("Could not retrieve codebase from API.")
            self.codebase: str = codebase_request
            

        # Initializing endpoints
        {%- for endpoint in endpoints %}
        self.{{ endpoint.field_name }} = {{ endpoint.class_name }}(self)
        {%- endfor %}

    def _get_url(self) -> str:
        \"""
        Generates and returns the URL for the ConnectWise Manage API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        \"""
        return f"https://{self.manage_url}/{self.codebase.strip('/')}/apis/3.0"

    def _try_get_codebase_from_api(self, manage_url: str, company_name: str, headers: dict[str, str]) -> str | None:
        \"""
        Tries to retrieve the codebase from the API using the provided company url, company name and headers.

        Parameters:
            company_url (str): URL of the company.
            company_name (str): Name of the company.
            headers (dict[str, str]): Headers to be sent in the request.

        Returns:
            str: Codebase string or None if an error occurs.
        \"""
        url = f"https://{manage_url}/login/companyinfo/{company_name}"
        response = self._make_request("GET", url, headers=headers)
        return response.json().get("Codebase")

    def _get_auth_string(self) -> str:
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

    def _get_headers(self) -> dict[str, str]:
        \"""
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        \"""
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self._get_auth_string(),
        }
        return headers

"""
)

automate_client_template = Template(
    """import base64
from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config
from datetime import datetime
{%- if imports is defined %}
{%- for import in imports %}
{{ import }}
{%- endfor %}
{%- endif %}

class ConnectWiseAutomateAPIClient(ConnectWiseClient):
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
        config: Config = None
    ):
        \"""
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            automate_url (str): URL of your ConnectWise Automate instance.
            client_id (str): Your ConnectWise Automate API Client ID.
            username (str): Your ConnectWise Automate API username.
            password (str): Your ConnectWise Automate API password.
            config (Config, optional): Optional additional configuration for API interactions.
        \"""
        self.client_id: str = client_id
        self.automate_url: str = automate_url
        self.username: str = username
        self.password: str = password
        self.token_expiry_time: datetime = datetime.utcnow()
        
        if config:
            self.config = config

        # Grab first access token
        self.access_token: str = self._get_access_token()
                
        # Initializing endpoints
        {%- for endpoint in endpoints %}
        self.{{ endpoint.field_name }} = {{ endpoint.class_name }}(self)
        {%- endfor %}

    def _get_url(self) -> str:
        \"""
        Generates and returns the URL for the ConnectWise Automate API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        \"""
        return f"https://{self.automate_url}/cwa/api/v1"

    def _get_access_token(self) -> str:
        \"""
        Performs a request to the ConnectWise Automate API to obtain an access token.
        \"""
        auth_response = self._make_request("POST", f"{self._get_url()}/apitoken", data={"UserName": self.username, "Password": self.password}, headers={"Content-Type": "application/json", "ClientId": self.client_id})
        auth_resp_json = auth_response.json()
        token = auth_resp_json["AccessToken"]
        self.token_expiry_time = datetime.fromisoformat(auth_resp_json["ExpirationDate"])
        return token
    
    def _refresh_access_token_if_necessary(self):
        if datetime.utcnow() > self.token_expiry_time:
            self.access_token = self._get_access_token()

    def _get_headers(self) -> dict[str, str]:
        \"""
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        \"""
        self._refresh_access_token_if_necessary()
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": f"Bearer {self.access_token}",
        }
        return headers

"""
)
