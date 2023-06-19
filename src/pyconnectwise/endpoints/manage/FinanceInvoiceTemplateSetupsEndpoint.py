from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplateSetupsIdEndpoint import FinanceInvoiceTemplateSetupsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplateSetupsCountEndpoint import FinanceInvoiceTemplateSetupsCountEndpoint
from pyconnectwise.models.manage.InvoiceTemplateSetupModel import InvoiceTemplateSetupModel

class FinanceInvoiceTemplateSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceTemplateSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoiceTemplateSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceInvoiceTemplateSetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoiceTemplateSetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoiceTemplateSetupsIdEndpoint: The initialized FinanceInvoiceTemplateSetupsIdEndpoint object.
        """
        child = FinanceInvoiceTemplateSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InvoiceTemplateSetupModel]:
        """
        Performs a GET request against the /finance/invoiceTemplateSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceTemplateSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InvoiceTemplateSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InvoiceTemplateSetupModel]:
        """
        Performs a GET request against the /finance/invoiceTemplateSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceTemplateSetupModel]: The parsed response data.
        """
        return self._parse_many(InvoiceTemplateSetupModel, super().make_request("GET", params=params).json())
        