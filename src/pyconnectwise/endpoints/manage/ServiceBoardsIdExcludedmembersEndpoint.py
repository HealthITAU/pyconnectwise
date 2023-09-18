from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdExcludedmembersCountEndpoint import \
    ServiceBoardsIdExcludedmembersCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdExcludedmembersIdEndpoint import \
    ServiceBoardsIdExcludedmembersIdEndpoint
from pyconnectwise.models.manage import BoardExcludedMember
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceBoardsIdExcludedmembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "excludedMembers", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdExcludedmembersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdExcludedmembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdExcludedmembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdExcludedmembersIdEndpoint: The initialized ServiceBoardsIdExcludedmembersIdEndpoint object.
        """
        child = ServiceBoardsIdExcludedmembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BoardExcludedMember]:
        """
        Performs a GET request against the /service/boards/{id}/excludedMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardExcludedMember]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardExcludedMember, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardExcludedMember]:
        """
        Performs a GET request against the /service/boards/{id}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardExcludedMember]: The parsed response data.
        """
        return self._parse_many(BoardExcludedMember, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardExcludedMember:
        """
        Performs a POST request against the /service/boards/{id}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardExcludedMember: The parsed response data.
        """
        return self._parse_one(BoardExcludedMember, super()._make_request("POST", data=data, params=params).json())
