from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesCountEndpoint import ServiceBoardsIdStatusesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdEndpoint import ServiceBoardsIdStatusesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesInfoEndpoint import ServiceBoardsIdStatusesInfoEndpoint
from pyconnectwise.models.manage import BoardStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceBoardsIdStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceBoardsIdStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceBoardsIdStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdStatusesIdEndpoint: The initialized ServiceBoardsIdStatusesIdEndpoint object.
        """
        child = ServiceBoardsIdStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardStatus]:
        """
        Performs a GET request against the /service/boards/{id}/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardStatus]:
        """
        Performs a GET request against the /service/boards/{id}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardStatus]: The parsed response data.
        """
        return self._parse_many(BoardStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardStatus:
        """
        Performs a POST request against the /service/boards/{id}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatus: The parsed response data.
        """
        return self._parse_one(BoardStatus, super()._make_request("POST", data=data, params=params).json())
