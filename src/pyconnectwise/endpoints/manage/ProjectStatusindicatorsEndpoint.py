from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsCountEndpoint import ProjectStatusindicatorsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsIdEndpoint import ProjectStatusindicatorsIdEndpoint
from pyconnectwise.models.manage import StatusIndicator
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectStatusindicatorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statusIndicators", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectStatusindicatorsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectStatusindicatorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectStatusindicatorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectStatusindicatorsIdEndpoint: The initialized ProjectStatusindicatorsIdEndpoint object.
        """
        child = ProjectStatusindicatorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[StatusIndicator]:
        """
        Performs a GET request against the /project/statusIndicators endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StatusIndicator]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), StatusIndicator, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[StatusIndicator]:
        """
        Performs a GET request against the /project/statusIndicators endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StatusIndicator]: The parsed response data.
        """
        return self._parse_many(StatusIndicator, super()._make_request("GET", data=data, params=params).json())
