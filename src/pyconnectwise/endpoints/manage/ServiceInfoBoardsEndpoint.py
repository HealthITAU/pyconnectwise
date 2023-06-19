from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceInfoBoardsIdEndpoint import ServiceInfoBoardsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardsCountEndpoint import ServiceInfoBoardsCountEndpoint
from pyconnectwise.models.manage.BoardInfoModel import BoardInfoModel

class ServiceInfoBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boards", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceInfoBoardsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceInfoBoardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceInfoBoardsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceInfoBoardsIdEndpoint: The initialized ServiceInfoBoardsIdEndpoint object.
        """
        child = ServiceInfoBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardInfoModel]:
        """
        Performs a GET request against the /service/info/boards endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardInfoModel]:
        """
        Performs a GET request against the /service/info/boards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardInfoModel]: The parsed response data.
        """
        return self._parse_many(BoardInfoModel, super().make_request("GET", params=params).json())
        