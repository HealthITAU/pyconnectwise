from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceGlAccountsIdEndpoint import FinanceGlAccountsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceGlAccountsCountEndpoint import FinanceGlAccountsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceGlAccountsMappedTypesEndpoint import FinanceGlAccountsMappedTypesEndpoint
from pyconnectwise.models.manage.GLAccountModel import GLAccountModel

class FinanceGlAccountsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glAccounts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlAccountsCountEndpoint(client, parent_endpoint=self)
        )
        self.mappedTypes = self.register_child_endpoint(
            FinanceGlAccountsMappedTypesEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceGlAccountsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlAccountsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceGlAccountsIdEndpoint: The initialized FinanceGlAccountsIdEndpoint object.
        """
        child = FinanceGlAccountsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GLAccountModel]:
        """
        Performs a GET request against the /finance/glAccounts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLAccountModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            GLAccountModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GLAccountModel]:
        """
        Performs a GET request against the /finance/glAccounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLAccountModel]: The parsed response data.
        """
        return self._parse_many(GLAccountModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GLAccountModel:
        """
        Performs a POST request against the /finance/glAccounts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLAccountModel: The parsed response data.
        """
        return self._parse_one(GLAccountModel, super().make_request("POST", params=params).json())
        