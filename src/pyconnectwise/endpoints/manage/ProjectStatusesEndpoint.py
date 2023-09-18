from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesCountEndpoint import ProjectStatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesIdEndpoint import ProjectStatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesInfoEndpoint import ProjectStatusesInfoEndpoint
from pyconnectwise.models.manage import ProjectStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProjectStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectStatusesIdEndpoint: The initialized ProjectStatusesIdEndpoint object.
        """
        child = ProjectStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectStatus]:
        """
        Performs a GET request against the /project/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectStatus]:
        """
        Performs a GET request against the /project/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectStatus]: The parsed response data.
        """
        return self._parse_many(ProjectStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectStatus:
        """
        Performs a POST request against the /project/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectStatus: The parsed response data.
        """
        return self._parse_one(ProjectStatus, super()._make_request("POST", data=data, params=params).json())
