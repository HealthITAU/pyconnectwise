from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint
from pyconnectwise.models.manage.ExpenseTypeExemptionModel import ExpenseTypeExemptionModel

class FinanceTaxCodesIdExpenseTypeExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expenseTypeExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint: The initialized FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint object.
        """
        child = FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseTypeExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/expenseTypeExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseTypeExemptionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExpenseTypeExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseTypeExemptionModel]:
        """
        Performs a GET request against the /finance/taxCodes/{parentId}/expenseTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseTypeExemptionModel]: The parsed response data.
        """
        return self._parse_many(ExpenseTypeExemptionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ExpenseTypeExemptionModel:
        """
        Performs a POST request against the /finance/taxCodes/{parentId}/expenseTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseTypeExemptionModel: The parsed response data.
        """
        return self._parse_one(ExpenseTypeExemptionModel, super().make_request("POST", params=params).json())
        