from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdInvoicesetupsCountEndpoint import \
    CompanyPortalconfigurationsIdInvoicesetupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint import \
    CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint
from pyconnectwise.models.manage import PortalConfigurationInvoiceSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsIdInvoicesetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsIdInvoicesetupsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint: The initialized CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsIdInvoicesetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationInvoiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PortalConfigurationInvoiceSetup]:
        """
        Performs a GET request against the /company/portalConfigurations/{id}/invoiceSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationInvoiceSetup]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationInvoiceSetup, super()._make_request("GET", data=data, params=params).json()
        )
