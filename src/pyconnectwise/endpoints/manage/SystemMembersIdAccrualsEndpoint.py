from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdAccrualsCountEndpoint import SystemMembersIdAccrualsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdAccrualsIdEndpoint import SystemMembersIdAccrualsIdEndpoint
from pyconnectwise.models.manage import MemberAccrual
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdAccrualsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accruals", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMembersIdAccrualsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembersIdAccrualsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdAccrualsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdAccrualsIdEndpoint: The initialized SystemMembersIdAccrualsIdEndpoint object.
        """
        child = SystemMembersIdAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MemberAccrual]:
        """
        Performs a GET request against the /system/members/{id}/accruals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberAccrual]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberAccrual, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberAccrual]:
        """
        Performs a GET request against the /system/members/{id}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberAccrual]: The parsed response data.
        """
        return self._parse_many(MemberAccrual, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberAccrual:
        """
        Performs a POST request against the /system/members/{id}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberAccrual: The parsed response data.
        """
        return self._parse_one(MemberAccrual, super()._make_request("POST", data=data, params=params).json())
