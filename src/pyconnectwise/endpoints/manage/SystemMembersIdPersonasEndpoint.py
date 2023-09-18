from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdPersonasCountEndpoint import SystemMembersIdPersonasCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdPersonasIdEndpoint import SystemMembersIdPersonasIdEndpoint
from pyconnectwise.models.manage import MemberPersona
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdPersonasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "personas", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMembersIdPersonasCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembersIdPersonasIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdPersonasIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdPersonasIdEndpoint: The initialized SystemMembersIdPersonasIdEndpoint object.
        """
        child = SystemMembersIdPersonasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MemberPersona]:
        """
        Performs a GET request against the /system/members/{id}/personas endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberPersona]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberPersona, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberPersona]:
        """
        Performs a GET request against the /system/members/{id}/personas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberPersona]: The parsed response data.
        """
        return self._parse_many(MemberPersona, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberPersona:
        """
        Performs a POST request against the /system/members/{id}/personas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberPersona: The parsed response data.
        """
        return self._parse_one(MemberPersona, super()._make_request("POST", data=data, params=params).json())
