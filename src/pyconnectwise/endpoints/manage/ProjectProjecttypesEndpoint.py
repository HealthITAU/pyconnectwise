from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesCountEndpoint import ProjectProjecttypesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesIdEndpoint import ProjectProjecttypesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttypesInfoEndpoint import ProjectProjecttypesInfoEndpoint
from pyconnectwise.models.manage import ProjectType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjecttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectProjecttypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProjectProjecttypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectProjecttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjecttypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjecttypesIdEndpoint: The initialized ProjectProjecttypesIdEndpoint object.
        """
        child = ProjectProjecttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectType]:
        """
        Performs a GET request against the /project/projectTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectType, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectType]:
        """
        Performs a GET request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectType]: The parsed response data.
        """
        return self._parse_many(ProjectType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectType:
        """
        Performs a POST request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectType: The parsed response data.
        """
        return self._parse_one(ProjectType, super()._make_request("POST", data=data, params=params).json())
