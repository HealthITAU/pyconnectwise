from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoardDefaultsIdEndpoint import FinanceAgreementsIdBoardDefaultsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoardDefaultsCountEndpoint import FinanceAgreementsIdBoardDefaultsCountEndpoint
from pyconnectwise.models.manage.BoardDefaultModel import BoardDefaultModel

class FinanceAgreementsIdBoardDefaultsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardDefaults", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdBoardDefaultsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementsIdBoardDefaultsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdBoardDefaultsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdBoardDefaultsIdEndpoint: The initialized FinanceAgreementsIdBoardDefaultsIdEndpoint object.
        """
        child = FinanceAgreementsIdBoardDefaultsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardDefaultModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/boardDefaults endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardDefaultModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardDefaultModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardDefaultModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardDefaultModel]: The parsed response data.
        """
        return self._parse_many(BoardDefaultModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardDefaultModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/boardDefaults endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardDefaultModel: The parsed response data.
        """
        return self._parse_one(BoardDefaultModel, super().make_request("POST", params=params).json())
        