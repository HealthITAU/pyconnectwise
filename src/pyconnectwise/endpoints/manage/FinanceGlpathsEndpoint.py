from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceGlpathsIdEndpoint import FinanceGlpathsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceGlpathsCountEndpoint import FinanceGlpathsCountEndpoint
from pyconnectwise.models.manage.GLPathModel import GLPathModel

class FinanceGlpathsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glpaths", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlpathsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceGlpathsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceGlpathsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceGlpathsIdEndpoint: The initialized FinanceGlpathsIdEndpoint object.
        """
        child = FinanceGlpathsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GLPathModel]:
        """
        Performs a GET request against the /finance/glpaths endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLPathModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            GLPathModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GLPathModel]:
        """
        Performs a GET request against the /finance/glpaths endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GLPathModel]: The parsed response data.
        """
        return self._parse_many(GLPathModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GLPathModel:
        """
        Performs a POST request against the /finance/glpaths endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLPathModel: The parsed response data.
        """
        return self._parse_one(GLPathModel, super().make_request("POST", params=params).json())
        