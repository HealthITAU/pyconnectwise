from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPdfEndpoint import FinanceInvoicesIdPdfEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPaymentsEndpoint import FinanceInvoicesIdPaymentsEndpoint
from pyconnectwise.models.manage.InvoiceModel import InvoiceModel

class FinanceInvoicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.pdf = self.register_child_endpoint(
            FinanceInvoicesIdPdfEndpoint(client, parent_endpoint=self)
        )
        self.payments = self.register_child_endpoint(
            FinanceInvoicesIdPaymentsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InvoiceModel]:
        """
        Performs a GET request against the /finance/invoices/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoiceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InvoiceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceModel:
        """
        Performs a GET request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceModel: The parsed response data.
        """
        return self._parse_one(InvoiceModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceModel:
        """
        Performs a PUT request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceModel: The parsed response data.
        """
        return self._parse_one(InvoiceModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoiceModel:
        """
        Performs a PATCH request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoiceModel: The parsed response data.
        """
        return self._parse_one(InvoiceModel, super().make_request("PATCH", params=params).json())
        