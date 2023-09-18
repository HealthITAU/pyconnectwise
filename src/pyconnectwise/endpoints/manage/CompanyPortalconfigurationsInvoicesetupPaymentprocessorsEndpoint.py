from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupPaymentprocessorsCountEndpoint import \
    CompanyPortalconfigurationsInvoicesetupPaymentprocessorsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint import \
    CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint
from pyconnectwise.models.manage import PortalConfigurationPaymentProcessor
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentProcessors", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupPaymentprocessorsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint: The initialized CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint object.
        """
        child = CompanyPortalconfigurationsInvoicesetupPaymentprocessorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalConfigurationPaymentProcessor]:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationPaymentProcessor]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalConfigurationPaymentProcessor,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PortalConfigurationPaymentProcessor]:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationPaymentProcessor]: The parsed response data.
        """
        return self._parse_many(
            PortalConfigurationPaymentProcessor, super()._make_request("GET", data=data, params=params).json()
        )
