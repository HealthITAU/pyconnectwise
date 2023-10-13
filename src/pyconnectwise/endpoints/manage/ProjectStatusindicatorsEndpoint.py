from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsCountEndpoint import ProjectStatusindicatorsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusindicatorsIdEndpoint import ProjectStatusindicatorsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import StatusIndicator
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectStatusindicatorsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[StatusIndicator], ConnectWiseManageRequestParams],
    IPaginateable[StatusIndicator, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "statusIndicators", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[StatusIndicator])
        IPaginateable.__init__(self, StatusIndicator)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), StatusIndicator, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[StatusIndicator]:
        """
        Performs a GET request against the /project/statusIndicators endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StatusIndicator]: The parsed response data.
        """
        return self._parse_many(StatusIndicator, super()._make_request("GET", data=data, params=params).json())
