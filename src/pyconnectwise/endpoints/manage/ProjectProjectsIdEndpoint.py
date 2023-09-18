from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdContactsEndpoint import ProjectProjectsIdContactsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesEndpoint import ProjectProjectsIdNotesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdPhasesEndpoint import ProjectProjectsIdPhasesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdProjectworkplanEndpoint import \
    ProjectProjectsIdProjectworkplanEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeammembersEndpoint import ProjectProjectsIdTeammembersEndpoint
from pyconnectwise.models.manage import Project
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjectsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.phases = self._register_child_endpoint(ProjectProjectsIdPhasesEndpoint(client, parent_endpoint=self))
        self.project_workplan = self._register_child_endpoint(
            ProjectProjectsIdProjectworkplanEndpoint(client, parent_endpoint=self)
        )
        self.team_members = self._register_child_endpoint(
            ProjectProjectsIdTeammembersEndpoint(client, parent_endpoint=self)
        )
        self.notes = self._register_child_endpoint(ProjectProjectsIdNotesEndpoint(client, parent_endpoint=self))
        self.contacts = self._register_child_endpoint(ProjectProjectsIdContactsEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Project]:
        """
        Performs a GET request against the /project/projects/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Project]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Project, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Project:
        """
        Performs a GET request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Project: The parsed response data.
        """
        return self._parse_one(Project, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Project:
        """
        Performs a PUT request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Project: The parsed response data.
        """
        return self._parse_one(Project, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Project:
        """
        Performs a PATCH request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Project: The parsed response data.
        """
        return self._parse_one(Project, super()._make_request("PATCH", data=data, params=params).json())
