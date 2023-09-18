from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemApimembersCountEndpoint import SystemApimembersCountEndpoint
from pyconnectwise.endpoints.manage.SystemApimembersDefaultEndpoint import SystemApimembersDefaultEndpoint
from pyconnectwise.endpoints.manage.SystemApimembersIdEndpoint import SystemApimembersIdEndpoint
from pyconnectwise.models.manage import ApiMember
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemApimembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "apiMembers", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemApimembersCountEndpoint(client, parent_endpoint=self))
        self.default = self._register_child_endpoint(SystemApimembersDefaultEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemApimembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemApimembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemApimembersIdEndpoint: The initialized SystemApimembersIdEndpoint object.
        """
        child = SystemApimembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ApiMember]:
        """
        Performs a GET request against the /system/apiMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ApiMember]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), ApiMember, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ApiMember]:
        """
        Performs a GET request against the /system/apiMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ApiMember]: The parsed response data.
        """
        return self._parse_many(ApiMember, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ApiMember:
        """
        Performs a POST request against the /system/apiMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ApiMember: The parsed response data.
        """
        return self._parse_one(ApiMember, super()._make_request("POST", data=data, params=params).json())
