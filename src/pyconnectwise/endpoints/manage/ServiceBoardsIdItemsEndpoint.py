from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsCountEndpoint import ServiceBoardsIdItemsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdEndpoint import ServiceBoardsIdItemsIdEndpoint
from pyconnectwise.models.manage import BoardItem
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceBoardsIdItemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "items", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceBoardsIdItemsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdItemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdItemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdItemsIdEndpoint: The initialized ServiceBoardsIdItemsIdEndpoint object.
        """
        child = ServiceBoardsIdItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardItem]:
        """
        Performs a GET request against the /service/boards/{id}/items endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardItem]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), BoardItem, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardItem]:
        """
        Performs a GET request against the /service/boards/{id}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardItem]: The parsed response data.
        """
        return self._parse_many(BoardItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardItem:
        """
        Performs a POST request against the /service/boards/{id}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItem: The parsed response data.
        """
        return self._parse_one(BoardItem, super()._make_request("POST", data=data, params=params).json())
