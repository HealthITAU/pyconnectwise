from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdNotificationsCountEndpoint import \
    CompanyManageddevicesintegrationsIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdNotificationsIdEndpoint import \
    CompanyManageddevicesintegrationsIdNotificationsIdEndpoint
from pyconnectwise.models.manage import ManagedDevicesIntegrationNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManageddevicesintegrationsIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManageddevicesintegrationsIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManageddevicesintegrationsIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManageddevicesintegrationsIdNotificationsIdEndpoint: The initialized CompanyManageddevicesintegrationsIdNotificationsIdEndpoint object.
        """
        child = CompanyManageddevicesintegrationsIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagedDevicesIntegrationNotification]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationNotification]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegrationNotification,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[ManagedDevicesIntegrationNotification]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationNotification]: The parsed response data.
        """
        return self._parse_many(
            ManagedDevicesIntegrationNotification, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ManagedDevicesIntegrationNotification:
        """
        Performs a POST request against the /company/managedDevicesIntegrations/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationNotification: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationNotification, super()._make_request("POST", data=data, params=params).json()
        )
