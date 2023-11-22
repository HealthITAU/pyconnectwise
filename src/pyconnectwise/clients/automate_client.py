import typing
from datetime import UTC, datetime

from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config

if typing.TYPE_CHECKING:
    from pyconnectwise.endpoints.automate.ClientsEndpoint import ClientsEndpoint
    from pyconnectwise.endpoints.automate.CommandsEndpoint import CommandsEndpoint
    from pyconnectwise.endpoints.automate.ComputersEndpoint import ComputersEndpoint
    from pyconnectwise.endpoints.automate.ContactsEndpoint import ContactsEndpoint
    from pyconnectwise.endpoints.automate.DataviewfoldersEndpoint import (
        DataviewfoldersEndpoint,
    )
    from pyconnectwise.endpoints.automate.DataviewsEndpoint import DataviewsEndpoint
    from pyconnectwise.endpoints.automate.DrivesEndpoint import DrivesEndpoint
    from pyconnectwise.endpoints.automate.ExternalsystemcredentialsEndpoint import (
        ExternalsystemcredentialsEndpoint,
    )
    from pyconnectwise.endpoints.automate.GroupsEndpoint import GroupsEndpoint
    from pyconnectwise.endpoints.automate.LocationsEndpoint import LocationsEndpoint
    from pyconnectwise.endpoints.automate.LookupsEndpoint import LookupsEndpoint
    from pyconnectwise.endpoints.automate.MonitorsEndpoint import MonitorsEndpoint
    from pyconnectwise.endpoints.automate.NetworkdevicesEndpoint import (
        NetworkdevicesEndpoint,
    )
    from pyconnectwise.endpoints.automate.PatchactionsEndpoint import PatchactionsEndpoint
    from pyconnectwise.endpoints.automate.PermissionsEndpoint import PermissionsEndpoint
    from pyconnectwise.endpoints.automate.ProbeconfigurationEndpoint import (
        ProbeconfigurationEndpoint,
    )
    from pyconnectwise.endpoints.automate.ScriptfoldersEndpoint import ScriptfoldersEndpoint
    from pyconnectwise.endpoints.automate.ScriptingEndpoint import ScriptingEndpoint
    from pyconnectwise.endpoints.automate.ScriptsEndpoint import ScriptsEndpoint
    from pyconnectwise.endpoints.automate.ServicesEndpoint import ServicesEndpoint
    from pyconnectwise.endpoints.automate.StatisticsEndpoint import StatisticsEndpoint
    from pyconnectwise.endpoints.automate.SystemEndpoint import SystemEndpoint
    from pyconnectwise.endpoints.automate.UserclassesEndpoint import UserclassesEndpoint
    from pyconnectwise.endpoints.automate.UsersEndpoint import UsersEndpoint


class ConnectWiseAutomateAPIClient(ConnectWiseClient):
    """
    ConnectWise Automate API client. Handles the connection to the ConnectWise Automate API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        automate_url: str,
        client_id: str,
        username: str,
        password: str,
        config: Config | None = None,
    ) -> None:
        """
        Initializes the client with the given credentials and optionally a specific codebase.
        If no codebase is given, it tries to get it from the API.

        Parameters:
            automate_url (str): URL of your ConnectWise Automate instance.
            client_id (str): Your ConnectWise Automate API Client ID.
            username (str): Your ConnectWise Automate API username.
            password (str): Your ConnectWise Automate API password.
            config (Config, optional): Optional additional configuration for API interactions.
        """
        self.client_id: str = client_id
        self.automate_url: str = automate_url
        self.username: str = username
        self.password: str = password
        self.token_expiry_time: datetime = datetime.now(tz=UTC)

        if config:
            self.config = config

        # Grab first access token
        self.access_token: str = self._get_access_token()

    # Initializing endpoints
    @property
    def commands(self) -> "CommandsEndpoint":
        from pyconnectwise.endpoints.automate import CommandsEndpoint

        return CommandsEndpoint(self)

    @property
    def clients(self) -> "ClientsEndpoint":
        from pyconnectwise.endpoints.automate import ClientsEndpoint

        return ClientsEndpoint(self)

    @property
    def computers(self) -> "ComputersEndpoint":
        from pyconnectwise.endpoints.automate import ComputersEndpoint

        return ComputersEndpoint(self)

    @property
    def services(self) -> "ServicesEndpoint":
        from pyconnectwise.endpoints.automate import ServicesEndpoint

        return ServicesEndpoint(self)

    @property
    def contacts(self) -> "ContactsEndpoint":
        from pyconnectwise.endpoints.automate import ContactsEndpoint

        return ContactsEndpoint(self)

    @property
    def dataviewfolders(self) -> "DataviewfoldersEndpoint":
        from pyconnectwise.endpoints.automate import DataviewfoldersEndpoint

        return DataviewfoldersEndpoint(self)

    @property
    def dataviews(self) -> "DataviewsEndpoint":
        from pyconnectwise.endpoints.automate import DataviewsEndpoint

        return DataviewsEndpoint(self)

    @property
    def groups(self) -> "GroupsEndpoint":
        from pyconnectwise.endpoints.automate import GroupsEndpoint

        return GroupsEndpoint(self)

    @property
    def monitors(self) -> "MonitorsEndpoint":
        from pyconnectwise.endpoints.automate import MonitorsEndpoint

        return MonitorsEndpoint(self)

    @property
    def networkdevices(self) -> "NetworkdevicesEndpoint":
        from pyconnectwise.endpoints.automate import NetworkdevicesEndpoint

        return NetworkdevicesEndpoint(self)

    @property
    def patchactions(self) -> "PatchactionsEndpoint":
        from pyconnectwise.endpoints.automate import PatchactionsEndpoint

        return PatchactionsEndpoint(self)

    @property
    def locations(self) -> "LocationsEndpoint":
        from pyconnectwise.endpoints.automate import LocationsEndpoint

        return LocationsEndpoint(self)

    @property
    def lookups(self) -> "LookupsEndpoint":
        from pyconnectwise.endpoints.automate import LookupsEndpoint

        return LookupsEndpoint(self)

    @property
    def probeconfiguration(self) -> "ProbeconfigurationEndpoint":
        from pyconnectwise.endpoints.automate import ProbeconfigurationEndpoint

        return ProbeconfigurationEndpoint(self)

    @property
    def scriptfolders(self) -> "ScriptfoldersEndpoint":
        from pyconnectwise.endpoints.automate import ScriptfoldersEndpoint

        return ScriptfoldersEndpoint(self)

    @property
    def scripting(self) -> "ScriptingEndpoint":
        from pyconnectwise.endpoints.automate import ScriptingEndpoint

        return ScriptingEndpoint(self)

    @property
    def scripts(self) -> "ScriptsEndpoint":
        from pyconnectwise.endpoints.automate import ScriptsEndpoint

        return ScriptsEndpoint(self)

    @property
    def drives(self) -> "DrivesEndpoint":
        from pyconnectwise.endpoints.automate import DrivesEndpoint

        return DrivesEndpoint(self)

    @property
    def statistics(self) -> "StatisticsEndpoint":
        from pyconnectwise.endpoints.automate import StatisticsEndpoint

        return StatisticsEndpoint(self)

    @property
    def system(self) -> "SystemEndpoint":
        from pyconnectwise.endpoints.automate import SystemEndpoint

        return SystemEndpoint(self)

    @property
    def externalsystemcredentials(self) -> "ExternalsystemcredentialsEndpoint":
        from pyconnectwise.endpoints.automate import ExternalsystemcredentialsEndpoint

        return ExternalsystemcredentialsEndpoint(self)

    @property
    def permissions(self) -> "PermissionsEndpoint":
        from pyconnectwise.endpoints.automate import PermissionsEndpoint

        return PermissionsEndpoint(self)

    @property
    def userclasses(self) -> "UserclassesEndpoint":
        from pyconnectwise.endpoints.automate import UserclassesEndpoint

        return UserclassesEndpoint(self)

    @property
    def users(self) -> "UsersEndpoint":
        from pyconnectwise.endpoints.automate import UsersEndpoint

        return UsersEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the ConnectWise Automate API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"https://{self.automate_url}/cwa/api/v1"

    def _get_access_token(self) -> str:
        """
        Performs a request to the ConnectWise Automate API to obtain an access token.
        """
        auth_response = self._make_request(
            "POST",
            f"{self._get_url()}/apitoken",
            data={"UserName": self.username, "Password": self.password},
            headers={"Content-Type": "application/json", "ClientId": self.client_id},
        )
        auth_resp_json = auth_response.json()
        token = auth_resp_json["AccessToken"]
        self.token_expiry_time = datetime.fromisoformat(auth_resp_json["ExpirationDate"])
        return token

    def _refresh_access_token_if_necessary(self):  # noqa: ANN202
        if datetime.now(tz=UTC) > self.token_expiry_time:
            self.access_token = self._get_access_token()

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        self._refresh_access_token_if_necessary()
        return {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": f"Bearer {self.access_token}",
        }
