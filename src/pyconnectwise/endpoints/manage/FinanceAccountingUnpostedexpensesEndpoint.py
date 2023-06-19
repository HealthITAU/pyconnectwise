from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdEndpoint import FinanceAccountingUnpostedexpensesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesCountEndpoint import FinanceAccountingUnpostedexpensesCountEndpoint
from pyconnectwise.models.manage.UnpostedExpenseModel import UnpostedExpenseModel

class FinanceAccountingUnpostedexpensesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedexpenses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedexpensesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedexpensesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedexpensesIdEndpoint: The initialized FinanceAccountingUnpostedexpensesIdEndpoint object.
        """
        child = FinanceAccountingUnpostedexpensesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedExpenseModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpenseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedExpenseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnpostedExpenseModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedExpenseModel]: The parsed response data.
        """
        return self._parse_many(UnpostedExpenseModel, super().make_request("GET", params=params).json())
        