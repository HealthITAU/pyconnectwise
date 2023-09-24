from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesCountEndpoint import ProjectStatusesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesIdEndpoint import ProjectStatusesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectStatusesInfoEndpoint import ProjectStatusesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectStatus], ConnectWiseManageRequestParams],
    IPostable[ProjectStatus, ConnectWiseManageRequestParams],
    IPaginateable[ProjectStatus, ConnectWiseManageRequestParams],
):
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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectStatus, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectStatus]:
        """
        Performs a GET request against the /project/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectStatus]: The parsed response data.
        """
        return self._parse_many(ProjectStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ProjectStatus:
        """
        Performs a POST request against the /project/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectStatus: The parsed response data.
        """
        return self._parse_one(ProjectStatus, super()._make_request("POST", data=data, params=params).json())
