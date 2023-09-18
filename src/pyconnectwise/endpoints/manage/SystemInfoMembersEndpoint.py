from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoMembersCountEndpoint import SystemInfoMembersCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoMembersIdEndpoint import SystemInfoMembersIdEndpoint
from pyconnectwise.models.manage import MemberInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemInfoMembersCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoMembersIdEndpoint: The initialized SystemInfoMembersIdEndpoint object.
        """
        child = SystemInfoMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberInfo]:
        """
        Performs a GET request against the /system/info/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), MemberInfo, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberInfo]:
        """
        Performs a GET request against the /system/info/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberInfo]: The parsed response data.
        """
        return self._parse_many(MemberInfo, super()._make_request("GET", data=data, params=params).json())
