from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsCountEndpoint import ProjectBoardsIdTeamsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdEndpoint import ProjectBoardsIdTeamsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsInfoEndpoint import ProjectBoardsIdTeamsInfoEndpoint
from pyconnectwise.models.manage import ProjectBoardTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectBoardsIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectBoardsIdTeamsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProjectBoardsIdTeamsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectBoardsIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBoardsIdTeamsIdEndpoint: The initialized ProjectBoardsIdTeamsIdEndpoint object.
        """
        child = ProjectBoardsIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectBoardTeam]:
        """
        Performs a GET request against the /project/boards/{id}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBoardTeam]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectBoardTeam, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectBoardTeam]:
        """
        Performs a GET request against the /project/boards/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBoardTeam]: The parsed response data.
        """
        return self._parse_many(ProjectBoardTeam, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeam:
        """
        Performs a POST request against the /project/boards/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeam: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeam, super()._make_request("POST", data=data, params=params).json())
