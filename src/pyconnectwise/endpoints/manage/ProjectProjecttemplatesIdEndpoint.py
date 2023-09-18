from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdProjecttemplateticketsEndpoint import \
    ProjectProjecttemplatesIdProjecttemplateticketsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjecttemplatesIdWorkplanEndpoint import \
    ProjectProjecttemplatesIdWorkplanEndpoint
from pyconnectwise.models.manage import ProjectTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjecttemplatesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.project_template_tickets = self._register_child_endpoint(
            ProjectProjecttemplatesIdProjecttemplateticketsEndpoint(client, parent_endpoint=self)
        )
        self.workplan = self._register_child_endpoint(
            ProjectProjecttemplatesIdWorkplanEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectTemplate]:
        """
        Performs a GET request against the /project/projectTemplates/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTemplate]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTemplate, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTemplate:
        """
        Performs a GET request against the /project/projectTemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTemplate: The parsed response data.
        """
        return self._parse_one(ProjectTemplate, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /project/projectTemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTemplate:
        """
        Performs a PUT request against the /project/projectTemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTemplate: The parsed response data.
        """
        return self._parse_one(ProjectTemplate, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTemplate:
        """
        Performs a PATCH request against the /project/projectTemplates/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTemplate: The parsed response data.
        """
        return self._parse_one(ProjectTemplate, super()._make_request("PATCH", data=data, params=params).json())
