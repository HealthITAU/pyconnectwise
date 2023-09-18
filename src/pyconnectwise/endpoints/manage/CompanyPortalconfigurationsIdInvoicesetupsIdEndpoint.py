from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint import \
    CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint
from pyconnectwise.models.manage import PortalConfigurationInvoiceSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.test_transaction = self._register_child_endpoint(
            CompanyPortalconfigurationsIdInvoicesetupsIdTesttransactionEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationInvoiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationInvoiceSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalConfigurationInvoiceSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetup:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup, super()._make_request("GET", data=data, params=params).json()
        )

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetup:
        """
        Performs a PUT request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalConfigurationInvoiceSetup:
        """
        Performs a PATCH request against the /company/portalConfigurations/{id}/invoiceSetups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalConfigurationInvoiceSetup: The parsed response data.
        """
        return self._parse_one(
            PortalConfigurationInvoiceSetup, super()._make_request("PATCH", data=data, params=params).json()
        )
