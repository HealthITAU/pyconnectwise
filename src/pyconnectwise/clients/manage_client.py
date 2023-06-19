import base64
import requests
from pyconnectwise.endpoints.manage.CompanyEndpoint import CompanyEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsEndpoint import ConfigurationsEndpoint
from pyconnectwise.endpoints.manage.ExpenseEndpoint import ExpenseEndpoint
from pyconnectwise.endpoints.manage.FinanceEndpoint import FinanceEndpoint
from pyconnectwise.endpoints.manage.MarketingEndpoint import MarketingEndpoint
from pyconnectwise.endpoints.manage.ProcurementEndpoint import ProcurementEndpoint
from pyconnectwise.endpoints.manage.ProjectEndpoint import ProjectEndpoint
from pyconnectwise.endpoints.manage.SalesEndpoint import SalesEndpoint
from pyconnectwise.endpoints.manage.ScheduleEndpoint import ScheduleEndpoint
from pyconnectwise.endpoints.manage.ServiceEndpoint import ServiceEndpoint
from pyconnectwise.endpoints.manage.SystemEndpoint import SystemEndpoint
from pyconnectwise.endpoints.manage.TimeEndpoint import TimeEndpoint

class ConnectWiseManageAPIClient:
    """
    ConnectWise Manage API client. Handles the connection to the ConnectWise Manage API
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
    ):
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
        """
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
        self.company = CompanyEndpoint(self)
        self.configurations = ConfigurationsEndpoint(self)
        self.expense = ExpenseEndpoint(self)
        self.finance = FinanceEndpoint(self)
        self.marketing = MarketingEndpoint(self)
        self.procurement = ProcurementEndpoint(self)
        self.project = ProjectEndpoint(self)
        self.sales = SalesEndpoint(self)
        self.schedule = ScheduleEndpoint(self)
        self.service = ServiceEndpoint(self)
        self.system = SystemEndpoint(self)
        self.time = TimeEndpoint(self)

    def get_url(self) -> str:
        """
        Generates and returns the URL for the ConnectWise Manage API endpoints based on the company url and codebase.

        Returns:
            str: API URL.
        """
        return f"https://{self.manage_url}/{self.codebase.strip('/')}/apis/3.0"

    def __try_get_codebase_from_api(self, manage_url: str, company_name: str, headers: dict[str, str]) -> str | None:
        """
        Tries to retrieve the codebase from the API using the provided company url, company name and headers.

        Parameters:
            company_url (str): URL of the company.
            company_name (str): Name of the company.
            headers (dict[str, str]): Headers to be sent in the request.

        Returns:
            str: Codebase string or None if an error occurs.
        """
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

    def get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        headers = {
            "Content-Type": "application/json",
            "clientId": self.client_id,
            "Authorization": self.__get_auth_string(),
        }
        return headers
