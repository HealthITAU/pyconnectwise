import json
import typing
from datetime import datetime, timedelta
from typing import Any

from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config
from pyconnectwise.endpoints.change_request import GetStatsEndpoint
from pyconnectwise.endpoints.change_request.AclsRolesEndpoint import AclsRolesEndpoint
from pyconnectwise.endpoints.change_request.LoginEndpoint import LoginEndpoint
from pyconnectwise.endpoints.change_request.SettingsEndpoint import SettingsEndpoint
from pyconnectwise.endpoints.change_request.TemplateEndpoint import TemplateEndpoint
from pyconnectwise.endpoints.change_request.UsersEndpoint import UsersEndpoint
from pyconnectwise.models.change_request import LoginMsg, LoginObject

if typing.TYPE_CHECKING:
    from pyconnectwise.endpoints.change_request.ChangeRequestsEndpoint import ChangeRequestsEndpoint
    from pyconnectwise.endpoints.change_request.ChangeTypeEndpoint import ChangeTypeEndpoint


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
        member_hash: str,
        member_id: str,
        login_username: str,
        login_password: str,
        login_role: str,
        login_partner_id: str,
        config: Config | None = None,
    ) -> None:
        """
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            company_name (str): Name of your company.
            manage_url (str): URL of your ConnectWise Change Approval instance.
            client_id (str): Your ConnectWise Manage API Client ID.
            public_key (str): Your ConnectWise Manage API Public key.
            private_key (str): Your ConnectWise Manage API Private key.
            config (Config, optional): Optional additional configuration for API interactions
        """
        self.login_msg: LoginMsg | None = None
        self.login_partner_id: str = login_partner_id
        self.login_role: str = login_role
        self.login_password: str = login_password
        self.login_username: str = login_username
        self.client_id: str = client_id
        self.company_name: str = company_name
        self.manage_url: str = manage_url
        self.member_hash: str = member_hash
        self.member_id: str = member_id
        self.__change_approval_cookie: str = ""
        self.__change_approval_cookie_expiration: datetime | None = None

        if config:
            self.config = config

    # Initializing endpoints
    @property
    def change_request(self) -> "ChangeRequestsEndpoint":
        from pyconnectwise.endpoints.change_request.ChangeRequestsEndpoint import ChangeRequestsEndpoint

        return ChangeRequestsEndpoint(self)

    @property
    def change_type(self) -> "ChangeTypeEndpoint":
        from pyconnectwise.endpoints.change_request.ChangeTypeEndpoint import ChangeTypeEndpoint

        return ChangeTypeEndpoint(self)

    @property
    def template(self) -> "TemplateEndpoint":
        from pyconnectwise.endpoints.change_request.TemplateEndpoint import TemplateEndpoint

        return TemplateEndpoint(self)

    @property
    def contacts(self):
        raise NotImplementedError("Contacts endpoint not implemented yet.")

    @property
    def acl_roles(self) -> "AclsRolesEndpoint":
        from pyconnectwise.endpoints.change_request.AclsRolesEndpoint import AclsRolesEndpoint

        return AclsRolesEndpoint(self)

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

    @property
    def users(self) -> "UsersEndpoint":
        from pyconnectwise.endpoints.change_request.UsersEndpoint import UsersEndpoint

        return UsersEndpoint(self)

    @property
    def login(self) -> "LoginEndpoint":
        from pyconnectwise.endpoints.change_request.LoginEndpoint import LoginEndpoint

        return LoginEndpoint(self)

    @property
    def settings(self) -> "SettingsEndpoint":
        from pyconnectwise.endpoints.change_request.SettingsEndpoint import SettingsEndpoint

        return SettingsEndpoint(self)

    @property
    def get_stats(self) -> "GetStatsEndpoint":
        from pyconnectwise.endpoints.change_request.GetStatsEndpoint import GetStatsEndpoint

        return GetStatsEndpoint(self)

    def auth_login(self) -> None:
        """
        Logs in to the ConnectWise Change Approval API and retrieves the new cookie
        """
        url = f"https://{self.manage_url}/api/login"
        login_data = {
            "userName": self.login_username,
            "password": self.login_password,
            "role": self.login_role,
            "partnerId": self.login_partner_id,
            "cwversion": "2024.1",  # TODO - Parameterize?
            "context": "web",
        }
        result = self._make_request("POST", url, data=login_data)
        result.raise_for_status()
        self.__change_approval_cookie = result.cookies["changeapproval"]
        login_obj = LoginObject.model_validate(result.json())
        self.login_msg = login_obj.msg
        # TODO - We get back expires=None, so log in every 6 hours?
        self.__change_approval_cookie_expiration = datetime.now() + timedelta(hours=6)

    def _get_cookies(self) -> dict[str, str]:
        """
        Generates and returns the cookies required for making API requests.

        Returns:
            dict[str, str]: Dictionary of cookies.
        """

        return {
            "companyName": self.company_name,
            "MemberID": self.member_id,
            "MemberHash": self.member_hash,
            "changeapproval": self.__change_approval_cookie,
        }

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the ConnectWise Manage API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        """
        return f"https://{self.manage_url}/api"

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "clientId": self.client_id,
        }

    def _get_query(self, x) -> dict[str, Any]:
        # Because ChangeApproval API is weird
        return {"query": json.dumps(x)}
