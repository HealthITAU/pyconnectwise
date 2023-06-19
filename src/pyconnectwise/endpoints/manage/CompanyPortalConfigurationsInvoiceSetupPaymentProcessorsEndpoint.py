from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint import CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint import CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint
from pyconnectwise.models.manage.PortalConfigurationPaymentProcessorModel import PortalConfigurationPaymentProcessorModel

class CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentProcessors", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint: The initialized CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint object.
        """
        child = CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PortalConfigurationPaymentProcessorModel]:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalConfigurationPaymentProcessorModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PortalConfigurationPaymentProcessorModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalConfigurationPaymentProcessorModel]:
        """
        Performs a GET request against the /company/portalConfigurations/invoiceSetup/paymentProcessors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalConfigurationPaymentProcessorModel]: The parsed response data.
        """
        return self._parse_many(PortalConfigurationPaymentProcessorModel, super().make_request("GET", params=params).json())
        