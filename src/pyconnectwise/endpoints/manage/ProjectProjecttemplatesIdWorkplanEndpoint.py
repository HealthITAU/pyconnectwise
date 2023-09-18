from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ProjectTemplateWorkPlan
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectProjecttemplatesIdWorkplanEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workplan", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProjectTemplateWorkPlan]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/workplan endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTemplateWorkPlan]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectTemplateWorkPlan, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectTemplateWorkPlan]:
        """
        Performs a GET request against the /project/projectTemplates/{id}/workplan endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTemplateWorkPlan]: The parsed response data.
        """
        return self._parse_many(ProjectTemplateWorkPlan, super()._make_request("GET", data=data, params=params).json())
