from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdMembersIdEndpoint import \
    ProjectBoardsIdTeamsIdMembersIdEndpoint
from pyconnectwise.models.manage import ProjectBoardTeamMember
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectBoardsIdTeamsIdMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ProjectBoardsIdTeamsIdMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdTeamsIdMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBoardsIdTeamsIdMembersIdEndpoint: The initialized ProjectBoardsIdTeamsIdMembersIdEndpoint object.
        """
        child = ProjectBoardsIdTeamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectBoardTeamMember]:
        """
        Performs a GET request against the /project/boards/{id}/teams/{id}/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBoardTeamMember]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectBoardTeamMember, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectBoardTeamMember]:
        """
        Performs a GET request against the /project/boards/{id}/teams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBoardTeamMember]: The parsed response data.
        """
        return self._parse_many(ProjectBoardTeamMember, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamMember:
        """
        Performs a POST request against the /project/boards/{id}/teams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamMember: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamMember, super()._make_request("POST", data=data, params=params).json())
