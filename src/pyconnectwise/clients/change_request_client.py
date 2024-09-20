import base64
import typing

from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config

if typing.TYPE_CHECKING:
    from pyconnectwise.endpoints.change_request.ChangeRequestEndpoint import ChangeRequestEndpoint


class ManageCodebaseError(Exception):
    def __init__(self) -> None:
        super().__init__("Could not retrieve codebase from API.")


class ConnectWiseChangeApprovalClient(ConnectWiseClient):
    """
    ConnectWise Change Approval API client. Handles the connection to the ConnectWise Change Approval API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        company_name: str,
        manage_url: str,
        client_id: str,
        public_key: str,
        private_key: str,
        codebase: str | None = None,
        config: Config | None = None,
    ) -> None:
        """
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
        """
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
                raise ManageCodebaseError()
            self.codebase: str = codebase_request

    # Initializing endpoints
    @property
    def change_request(self) -> "ChangeRequestEndpoint":
        from pyconnectwise.endpoints.change_request.ChangeRequestEndpoint import ChangeRequestEndpoint

        return ChangeRequestEndpoint(self)

    @property
    def change_type(self) -> "ChangeTypeEndpoint":
        from pyconnectwise.endpoints.change_request.ChangeTypeEndpoint import ChangeTypeEndpoint

        return ChangeTypeEndpoint(self)

    @property
    def contacts(self):
        raise NotImplementedError("Contacts endpoint not implemented yet.")

    @property
    def configurations(self):
        raise NotImplementedError("Configurations endpoint not implemented yet.")

    @property
    def members(self):
        raise NotImplementedError("Members endpoint not implemented yet.")

    @property
    def company(self):
        # TODO: /company/{id}/getSites
        raise NotImplementedError("Company endpoint not implemented yet.")

    @property
    def audit_logs(self):
        raise NotImplementedError("Audit Logs endpoint not implemented yet.")

    @property
    def approval_groups(self):
        raise NotImplementedError("approval groups endpoint not implemented yet.")

    @property
    def audit_log(self):
        # Yes, this has a different route than the plural version
        raise NotImplementedError("audit log singular endpoint not implemented yet.")

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the ConnectWise Manage API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        """
        return f"https://{self.manage_url}/{self.codebase.strip('/')}/api"

    def _try_get_codebase_from_api(self, manage_url: str, company_name: str, headers: dict[str, str]) -> str:
        """
        Tries to retrieve the codebase from the API using the provided company url, company name and headers.

        Parameters:
            company_url (str): URL of the company.
            company_name (str): Name of the company.
            headers (dict[str, str]): Headers to be sent in the request.

        Returns:
            str: Codebase string or None if an error occurs.
        """
        url = f"https://{manage_url}/login/companyinfo/{company_name}"
        response = self._make_request("GET", url, headers=headers)
        return response.json().get("Codebase")

    def _get_auth_string(self) -> str:
        """
        Creates and returns the base64 encoded authorization string required for API requests.

        Returns:
            str: Base64 encoded authorization string.
        """
        return "Basic " + base64.b64encode(
            bytes(
                f"{self.company_name}+{self.public_key}:{self.private_key}",
                encoding="utf8",
            )
        ).decode("ascii")

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self._get_auth_string(),
        }
