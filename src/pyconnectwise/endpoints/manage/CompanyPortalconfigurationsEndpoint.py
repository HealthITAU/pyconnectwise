from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsCopyEndpoint import \
    CompanyPortalconfigurationsCopyEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsCountEndpoint import \
    CompanyPortalconfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdEndpoint import CompanyPortalconfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupEndpoint import \
    CompanyPortalconfigurationsInvoicesetupEndpoint
from pyconnectwise.models.manage import PortalConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalConfigurations", parent_endpoint=parent_endpoint)

        self.copy = self._register_child_endpoint(CompanyPortalconfigurationsCopyEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsCountEndpoint(client, parent_endpoint=self)
        )
        self.invoice_setup = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdEndpoint: The initialized CompanyPortalconfigurationsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfiguration]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfiguration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfiguration, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfiguration]:
        """
        Performs a GET request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfiguration]: The parsed response data.
        """
        return self._parse_many(PortalConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfiguration:
        """
        Performs a POST request against the /company/portalConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfiguration: The parsed response data.
        """
        return self._parse_one(PortalConfiguration, super()._make_request("POST", data=data, params=params).json())
