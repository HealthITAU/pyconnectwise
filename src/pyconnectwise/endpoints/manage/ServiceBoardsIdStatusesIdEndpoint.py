from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdNotificationsEndpoint import ServiceBoardsIdStatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdInfoEndpoint import ServiceBoardsIdStatusesIdInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdUsagesEndpoint import ServiceBoardsIdStatusesIdUsagesEndpoint
from pyconnectwise.models.manage.BoardStatusModel import BoardStatusModel

class ServiceBoardsIdStatusesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.notifications = self.register_child_endpoint(
            ServiceBoardsIdStatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceBoardsIdStatusesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ServiceBoardsIdStatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardStatusModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardStatusModel:
        """
        Performs a GET request against the /service/boards/{parentId}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatusModel: The parsed response data.
        """
        return self._parse_one(BoardStatusModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /service/boards/{parentId}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardStatusModel:
        """
        Performs a PUT request against the /service/boards/{parentId}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatusModel: The parsed response data.
        """
        return self._parse_one(BoardStatusModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardStatusModel:
        """
        Performs a PATCH request against the /service/boards/{parentId}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatusModel: The parsed response data.
        """
        return self._parse_one(BoardStatusModel, super().make_request("PATCH", params=params).json())
        