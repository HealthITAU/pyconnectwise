from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdInfoEndpoint import ProjectBoardsIdTeamsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdMembersEndpoint import ProjectBoardsIdTeamsIdMembersEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import ProjectBoardTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProjectBoardsIdTeamsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ProjectBoardTeam, ConnectWiseManageRequestParams],
    IPatchable[ProjectBoardTeam, ConnectWiseManageRequestParams],
    IPuttable[ProjectBoardTeam, ConnectWiseManageRequestParams],
    IPaginateable[ProjectBoardTeam, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ProjectBoardTeam)
        IPatchable.__init__(self, ProjectBoardTeam)
        IPuttable.__init__(self, ProjectBoardTeam)
        IPaginateable.__init__(self, ProjectBoardTeam)

        self.info = self._register_child_endpoint(ProjectBoardsIdTeamsIdInfoEndpoint(client, parent_endpoint=self))
        self.members = self._register_child_endpoint(
            ProjectBoardsIdTeamsIdMembersEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectBoardTeam]:
        """
        Performs a GET request against the /project/boards/{id}/teams/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBoardTeam]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectBoardTeam, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /project/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectBoardTeam:
        """
        Performs a GET request against the /project/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeam: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeam, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ProjectBoardTeam:
        """
        Performs a PATCH request against the /project/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeam: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeam, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectBoardTeam:
        """
        Performs a PUT request against the /project/boards/{id}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeam: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeam, super()._make_request("PUT", data=data, params=params).json())
