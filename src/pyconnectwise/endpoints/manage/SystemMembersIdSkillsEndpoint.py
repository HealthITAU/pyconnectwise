from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSkillsCountEndpoint import SystemMembersIdSkillsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSkillsIdEndpoint import SystemMembersIdSkillsIdEndpoint
from pyconnectwise.models.manage import MemberSkill
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdSkillsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skills", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMembersIdSkillsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembersIdSkillsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdSkillsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdSkillsIdEndpoint: The initialized SystemMembersIdSkillsIdEndpoint object.
        """
        child = SystemMembersIdSkillsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberSkill]:
        """
        Performs a GET request against the /system/members/{id}/skills endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberSkill]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberSkill, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberSkill]:
        """
        Performs a GET request against the /system/members/{id}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberSkill]: The parsed response data.
        """
        return self._parse_many(MemberSkill, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberSkill:
        """
        Performs a POST request against the /system/members/{id}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberSkill: The parsed response data.
        """
        return self._parse_one(MemberSkill, super()._make_request("POST", data=data, params=params).json())
