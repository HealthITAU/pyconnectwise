import base64
from datetime import datetime

from pyconnectwise.clients.connectwise_client import ConnectWiseClient
from pyconnectwise.config import Config
from pyconnectwise.endpoints.automate.ClientsEndpoint import ClientsEndpoint
from pyconnectwise.endpoints.automate.CommandsEndpoint import CommandsEndpoint
from pyconnectwise.endpoints.automate.ComputersEndpoint import ComputersEndpoint
from pyconnectwise.endpoints.automate.ContactsEndpoint import ContactsEndpoint
from pyconnectwise.endpoints.automate.DataviewfoldersEndpoint import DataviewfoldersEndpoint
from pyconnectwise.endpoints.automate.DataviewsEndpoint import DataviewsEndpoint
from pyconnectwise.endpoints.automate.DrivesEndpoint import DrivesEndpoint
from pyconnectwise.endpoints.automate.ExternalsystemcredentialsEndpoint import ExternalsystemcredentialsEndpoint
from pyconnectwise.endpoints.automate.GroupsEndpoint import GroupsEndpoint
from pyconnectwise.endpoints.automate.LocationsEndpoint import LocationsEndpoint
from pyconnectwise.endpoints.automate.LookupsEndpoint import LookupsEndpoint
from pyconnectwise.endpoints.automate.MonitorsEndpoint import MonitorsEndpoint
from pyconnectwise.endpoints.automate.NetworkdevicesEndpoint import NetworkdevicesEndpoint
from pyconnectwise.endpoints.automate.PatchactionsEndpoint import PatchactionsEndpoint
from pyconnectwise.endpoints.automate.PermissionsEndpoint import PermissionsEndpoint
from pyconnectwise.endpoints.automate.ProbeconfigurationEndpoint import ProbeconfigurationEndpoint
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

    def __init__(self, automate_url: str, client_id: str, username: str, password: str, config: Config = None):
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
        self.token_expiry_time: datetime = datetime.utcnow()

        if config:
            self.config = config

        # Grab first access token
        self.access_token: str = self._get_access_token()

        # Initializing endpoints
        self.commands = CommandsEndpoint(self)
        self.clients = ClientsEndpoint(self)
        self.computers = ComputersEndpoint(self)
        self.services = ServicesEndpoint(self)
        self.contacts = ContactsEndpoint(self)
        self.dataviewfolders = DataviewfoldersEndpoint(self)
        self.dataviews = DataviewsEndpoint(self)
        self.groups = GroupsEndpoint(self)
        self.monitors = MonitorsEndpoint(self)
        self.networkdevices = NetworkdevicesEndpoint(self)
        self.patchactions = PatchactionsEndpoint(self)
        self.locations = LocationsEndpoint(self)
        self.lookups = LookupsEndpoint(self)
        self.probeconfiguration = ProbeconfigurationEndpoint(self)
        self.scriptfolders = ScriptfoldersEndpoint(self)
        self.scripting = ScriptingEndpoint(self)
        self.scripts = ScriptsEndpoint(self)
        self.drives = DrivesEndpoint(self)
        self.statistics = StatisticsEndpoint(self)
        self.system = SystemEndpoint(self)
        self.externalsystemcredentials = ExternalsystemcredentialsEndpoint(self)
        self.permissions = PermissionsEndpoint(self)
        self.userclasses = UserclassesEndpoint(self)
        self.users = UsersEndpoint(self)

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

    def _refresh_access_token_if_necessary(self):
        if datetime.utcnow() > self.token_expiry_time:
            self.access_token = self._get_access_token()

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        self._refresh_access_token_if_necessary()
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": f"Bearer {self.access_token}",
        }
        return headers
