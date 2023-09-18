from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdCrossreferencesCountEndpoint import \
    CompanyManageddevicesintegrationsIdCrossreferencesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint import \
    CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint
from pyconnectwise.models.manage import ManagedDevicesIntegrationCrossReference
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManageddevicesintegrationsIdCrossreferencesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "crossReferences", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyManageddevicesintegrationsIdCrossreferencesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint: The initialized CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint object.
        """
        child = CompanyManageddevicesintegrationsIdCrossreferencesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ManagedDevicesIntegrationCrossReference]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/crossReferences endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationCrossReference]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagedDevicesIntegrationCrossReference,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[ManagedDevicesIntegrationCrossReference]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{id}/crossReferences endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagedDevicesIntegrationCrossReference]: The parsed response data.
        """
        return self._parse_many(
            ManagedDevicesIntegrationCrossReference, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ManagedDevicesIntegrationCrossReference:
        """
        Performs a POST request against the /company/managedDevicesIntegrations/{id}/crossReferences endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReference: The parsed response data.
        """
        return self._parse_one(
            ManagedDevicesIntegrationCrossReference, super()._make_request("POST", data=data, params=params).json()
        )
