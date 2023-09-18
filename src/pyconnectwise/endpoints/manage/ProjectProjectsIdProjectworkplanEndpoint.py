from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdProjectworkplanCountEndpoint import \
    ProjectProjectsIdProjectworkplanCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdProjectworkplanIdEndpoint import \
    ProjectProjectsIdProjectworkplanIdEndpoint
from pyconnectwise.models.manage import ProjectWorkplan
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjectsIdProjectworkplanEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectWorkplan", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProjectProjectsIdProjectworkplanCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProjectProjectsIdProjectworkplanIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdProjectworkplanIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdProjectworkplanIdEndpoint: The initialized ProjectProjectsIdProjectworkplanIdEndpoint object.
        """
        child = ProjectProjectsIdProjectworkplanIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectWorkplan]:
        """
        Performs a GET request against the /project/projects/{id}/projectWorkplan endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectWorkplan]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectWorkplan, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectWorkplan]:
        """
        Performs a GET request against the /project/projects/{id}/projectWorkplan endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectWorkplan]: The parsed response data.
        """
        return self._parse_many(ProjectWorkplan, super()._make_request("GET", data=data, params=params).json())
