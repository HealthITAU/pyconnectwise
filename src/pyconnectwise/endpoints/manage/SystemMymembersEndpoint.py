from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMymembersInfoEndpoint import SystemMymembersInfoEndpoint
from pyconnectwise.models.manage import MyMember
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMymembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "myMembers", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemMymembersInfoEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MyMember]:
        """
        Performs a GET request against the /system/myMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MyMember]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), MyMember, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyMember:
        """
        Performs a GET request against the /system/myMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyMember: The parsed response data.
        """
        return self._parse_one(MyMember, super()._make_request("GET", data=data, params=params).json())
