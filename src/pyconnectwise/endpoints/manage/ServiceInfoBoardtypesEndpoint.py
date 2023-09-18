from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesCountEndpoint import ServiceInfoBoardtypesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesIdEndpoint import ServiceInfoBoardtypesIdEndpoint
from pyconnectwise.models.manage import BoardTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceInfoBoardtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "boardtypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceInfoBoardtypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceInfoBoardtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceInfoBoardtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceInfoBoardtypesIdEndpoint: The initialized ServiceInfoBoardtypesIdEndpoint object.
        """
        child = ServiceInfoBoardtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BoardTypeInfo]:
        """
        Performs a GET request against the /service/info/boardtypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTypeInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardTypeInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardTypeInfo]:
        """
        Performs a GET request against the /service/info/boardtypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardTypeInfo]: The parsed response data.
        """
        return self._parse_many(BoardTypeInfo, super()._make_request("GET", data=data, params=params).json())
