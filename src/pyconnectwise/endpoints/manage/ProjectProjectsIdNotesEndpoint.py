from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesCountEndpoint import ProjectProjectsIdNotesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesIdEndpoint import ProjectProjectsIdNotesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectNote
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjectsIdNotesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectNote], ConnectWiseManageRequestParams],
    IPostable[ProjectNote, ConnectWiseManageRequestParams],
    IPaginateable[ProjectNote, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProjectNote])
        IPostable.__init__(self, ProjectNote)
        IPaginateable.__init__(self, ProjectNote)

        self.count = self._register_child_endpoint(ProjectProjectsIdNotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectProjectsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdNotesIdEndpoint: The initialized ProjectProjectsIdNotesIdEndpoint object.
        """
        child = ProjectProjectsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectNote]:
        """
        Performs a GET request against the /project/projects/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectNote]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectNote, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ProjectNote]:
        """
        Performs a GET request against the /project/projects/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectNote]: The parsed response data.
        """
        return self._parse_many(ProjectNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectNote:
        """
        Performs a POST request against the /project/projects/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectNote: The parsed response data.
        """
        return self._parse_one(ProjectNote, super()._make_request("POST", data=data, params=params).json())
