from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdEndpoint import ServiceBoardsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsCopyEndpoint import ServiceBoardsCopyEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsCountEndpoint import ServiceBoardsCountEndpoint
from pyconnectwise.models.manage.BoardModel import BoardModel

class ServiceBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boards", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            ServiceBoardsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            ServiceBoardsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdEndpoint: The initialized ServiceBoardsIdEndpoint object.
        """
        child = ServiceBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardModel]:
        """
        Performs a GET request against the /service/boards endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardModel]:
        """
        Performs a GET request against the /service/boards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardModel]: The parsed response data.
        """
        return self._parse_many(BoardModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardModel:
        """
        Performs a POST request against the /service/boards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardModel: The parsed response data.
        """
        return self._parse_one(BoardModel, super().make_request("POST", params=params).json())
        