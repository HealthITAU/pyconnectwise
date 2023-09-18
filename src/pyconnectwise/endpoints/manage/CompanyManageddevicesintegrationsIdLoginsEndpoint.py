from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdLoginsCountEndpoint import \
    CompanyManageddevicesintegrationsIdLoginsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdLoginsIdEndpoint import \
    CompanyManageddevicesintegrationsIdLoginsIdEndpoint
from pyconnectwise.models.manage import ManagedDevicesIntegrationLogin
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManageddevicesintegrationsIdLoginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "logins", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdLoginsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManageddevicesintegrationsIdLoginsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManageddevicesintegrationsIdLoginsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManageddevicesintegrationsIdLoginsIdEndpoint: The initialized CompanyManageddevicesintegrationsIdLoginsIdEndpoint object.
        """
        child = CompanyManageddevicesintegrationsIdLoginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagedDevicesIntegrationLogin]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/logins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationLogin]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagedDevicesIntegrationLogin, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagedDevicesIntegrationLogin]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/logins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationLogin]: The parsed response data.
        """
        return self._parse_many(
            ManagedDevicesIntegrationLogin, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationLogin:
        """
        Performs a POST request against the /company/managedDevicesIntegrations/{id}/logins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationLogin: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationLogin, super()._make_request("POST", data=data, params=params).json()
        )
