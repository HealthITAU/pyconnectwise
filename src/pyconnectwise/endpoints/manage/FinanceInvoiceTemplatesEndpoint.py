from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplatesIdEndpoint import FinanceInvoiceTemplatesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoiceTemplatesCountEndpoint import FinanceInvoiceTemplatesCountEndpoint
from pyconnectwise.models.manage.InvoiceTemplateModel import InvoiceTemplateModel

class FinanceInvoiceTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoiceTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceInvoiceTemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoiceTemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoiceTemplatesIdEndpoint: The initialized FinanceInvoiceTemplatesIdEndpoint object.
        """
        child = FinanceInvoiceTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InvoiceTemplateModel]:
        """
        Performs a GET request against the /finance/invoiceTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InvoiceTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InvoiceTemplateModel]:
        """
        Performs a GET request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoiceTemplateModel]: The parsed response data.
        """
        return self._parse_many(InvoiceTemplateModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceTemplateModel:
        """
        Performs a POST request against the /finance/invoiceTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceTemplateModel: The parsed response data.
        """
        return self._parse_one(InvoiceTemplateModel, super().make_request("POST", params=params).json())
        