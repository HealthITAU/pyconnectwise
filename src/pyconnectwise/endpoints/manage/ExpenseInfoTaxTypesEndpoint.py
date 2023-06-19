from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ExpenseInfoTaxTypesIdEndpoint import ExpenseInfoTaxTypesIdEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoTaxTypesCountEndpoint import ExpenseInfoTaxTypesCountEndpoint
from pyconnectwise.models.manage.ExpenseTaxTypeInfoModel import ExpenseTaxTypeInfoModel

class ExpenseInfoTaxTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseInfoTaxTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ExpenseInfoTaxTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseInfoTaxTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseInfoTaxTypesIdEndpoint: The initialized ExpenseInfoTaxTypesIdEndpoint object.
        """
        child = ExpenseInfoTaxTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseTaxTypeInfoModel]:
        """
        Performs a GET request against the /expense/info/taxTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseTaxTypeInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExpenseTaxTypeInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseTaxTypeInfoModel]:
        """
        Performs a GET request against the /expense/info/taxTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseTaxTypeInfoModel]: The parsed response data.
        """
        return self._parse_many(ExpenseTaxTypeInfoModel, super().make_request("GET", params=params).json())
        