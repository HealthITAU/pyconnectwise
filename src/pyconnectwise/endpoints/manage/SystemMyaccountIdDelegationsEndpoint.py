from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdDelegationsCountEndpoint import \
    SystemMyaccountIdDelegationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdDelegationsIdEndpoint import SystemMyaccountIdDelegationsIdEndpoint
from pyconnectwise.models.manage import MemberDelegation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMyaccountIdDelegationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "delegations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemMyaccountIdDelegationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMyaccountIdDelegationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyaccountIdDelegationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyaccountIdDelegationsIdEndpoint: The initialized SystemMyaccountIdDelegationsIdEndpoint object.
        """
        child = SystemMyaccountIdDelegationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MemberDelegation]:
        """
        Performs a GET request against the /system/myAccount/{id}/delegations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberDelegation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberDelegation, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberDelegation]:
        """
        Performs a GET request against the /system/myAccount/{id}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberDelegation]: The parsed response data.
        """
        return self._parse_many(MemberDelegation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberDelegation:
        """
        Performs a POST request against the /system/myAccount/{id}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberDelegation: The parsed response data.
        """
        return self._parse_one(MemberDelegation, super()._make_request("POST", data=data, params=params).json())
