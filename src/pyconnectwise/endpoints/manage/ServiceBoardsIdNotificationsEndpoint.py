from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdNotificationsIdEndpoint import ServiceBoardsIdNotificationsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdNotificationsCountEndpoint import ServiceBoardsIdNotificationsCountEndpoint
from pyconnectwise.models.manage.BoardNotificationModel import BoardNotificationModel

class ServiceBoardsIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdNotificationsIdEndpoint: The initialized ServiceBoardsIdNotificationsIdEndpoint object.
        """
        child = ServiceBoardsIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardNotificationModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardNotificationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardNotificationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardNotificationModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardNotificationModel]: The parsed response data.
        """
        return self._parse_many(BoardNotificationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardNotificationModel:
        """
        Performs a POST request against the /service/boards/{parentId}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardNotificationModel: The parsed response data.
        """
        return self._parse_one(BoardNotificationModel, super().make_request("POST", params=params).json())
        