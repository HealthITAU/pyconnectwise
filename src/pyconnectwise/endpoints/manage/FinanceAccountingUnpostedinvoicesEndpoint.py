from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesIdEndpoint import FinanceAccountingUnpostedinvoicesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesCountEndpoint import FinanceAccountingUnpostedinvoicesCountEndpoint
from pyconnectwise.models.manage.UnpostedInvoiceModel import UnpostedInvoiceModel

class FinanceAccountingUnpostedinvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedinvoices", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedinvoicesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingUnpostedinvoicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedinvoicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedinvoicesIdEndpoint: The initialized FinanceAccountingUnpostedinvoicesIdEndpoint object.
        """
        child = FinanceAccountingUnpostedinvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedInvoiceModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedInvoiceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedInvoiceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnpostedInvoiceModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedInvoiceModel]: The parsed response data.
        """
        return self._parse_many(UnpostedInvoiceModel, super().make_request("GET", params=params).json())
        