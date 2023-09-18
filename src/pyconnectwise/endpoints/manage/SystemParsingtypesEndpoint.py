from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemParsingtypesCountEndpoint import SystemParsingtypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemParsingtypesIdEndpoint import SystemParsingtypesIdEndpoint
from pyconnectwise.models.manage import ParsingType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemParsingtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemParsingtypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemParsingtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemParsingtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemParsingtypesIdEndpoint: The initialized SystemParsingtypesIdEndpoint object.
        """
        child = SystemParsingtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ParsingType]:
        """
        Performs a GET request against the /system/parsingTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ParsingType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ParsingType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ParsingType]:
        """
        Performs a GET request against the /system/parsingTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ParsingType]: The parsed response data.
        """
        return self._parse_many(ParsingType, super()._make_request("GET", data=data, params=params).json())
