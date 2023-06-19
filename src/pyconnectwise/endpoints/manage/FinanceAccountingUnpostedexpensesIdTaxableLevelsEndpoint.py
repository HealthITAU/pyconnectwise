from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint import FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint import FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint
from pyconnectwise.models.manage.UnpostedExpenseTaxableLevelModel import UnpostedExpenseTaxableLevelModel

class FinanceAccountingUnpostedexpensesIdTaxableLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint: The initialized FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint object.
        """
        child = FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnpostedExpenseTaxableLevelModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{parentId}/taxableLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpenseTaxableLevelModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnpostedExpenseTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnpostedExpenseTaxableLevelModel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{parentId}/taxableLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedExpenseTaxableLevelModel]: The parsed response data.
        """
        return self._parse_many(UnpostedExpenseTaxableLevelModel, super().make_request("GET", params=params).json())
        