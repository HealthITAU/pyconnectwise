from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeammembersCountEndpoint import \
    ProjectProjectsIdTeammembersCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeammembersIdEndpoint import ProjectProjectsIdTeammembersIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectTeamMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjectsIdTeammembersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectTeamMember], ConnectWiseManageRequestParams],
    IPostable[ProjectTeamMember, ConnectWiseManageRequestParams],
    IPaginateable[ProjectTeamMember, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "teamMembers", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectTeamMember])
        IPostable.__init__(self, ProjectTeamMember)
        IPaginateable.__init__(self, ProjectTeamMember)

        self.count = self._register_child_endpoint(
            ProjectProjectsIdTeammembersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectProjectsIdTeammembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdTeammembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdTeammembersIdEndpoint: The initialized ProjectProjectsIdTeammembersIdEndpoint object.
        """
        child = ProjectProjectsIdTeammembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectTeamMember]:
        """
        Performs a GET request against the /project/projects/{id}/teamMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTeamMember]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTeamMember, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectTeamMember]:
        """
        Performs a GET request against the /project/projects/{id}/teamMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTeamMember]: The parsed response data.
        """
        return self._parse_many(ProjectTeamMember, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectTeamMember:
        """
        Performs a POST request against the /project/projects/{id}/teamMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTeamMember: The parsed response data.
        """
        return self._parse_one(ProjectTeamMember, super()._make_request("POST", data=data, params=params).json())
