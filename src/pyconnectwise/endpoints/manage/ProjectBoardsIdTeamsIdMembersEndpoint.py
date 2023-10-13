from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdMembersIdEndpoint import \
    ProjectBoardsIdTeamsIdMembersIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectBoardTeamMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectBoardsIdTeamsIdMembersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectBoardTeamMember], ConnectWiseManageRequestParams],
    IPostable[ProjectBoardTeamMember, ConnectWiseManageRequestParams],
    IPaginateable[ProjectBoardTeamMember, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "members", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectBoardTeamMember])
        IPostable.__init__(self, ProjectBoardTeamMember)
        IPaginateable.__init__(self, ProjectBoardTeamMember)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectBoardTeamMember, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectBoardTeamMember]:
        """
        Performs a GET request against the /project/boards/{id}/teams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBoardTeamMember]: The parsed response data.
        """
        return self._parse_many(ProjectBoardTeamMember, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectBoardTeamMember:
        """
        Performs a POST request against the /project/boards/{id}/teams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamMember: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamMember, super()._make_request("POST", data=data, params=params).json())
