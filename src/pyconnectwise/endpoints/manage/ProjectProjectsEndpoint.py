from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsCountEndpoint import ProjectProjectsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdEndpoint import ProjectProjectsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Project
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectProjectsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Project], ConnectWiseManageRequestParams],
    IPostable[Project, ConnectWiseManageRequestParams],
    IPaginateable[Project, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "projects", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Project])
        IPostable.__init__(self, Project)
        IPaginateable.__init__(self, Project)

        self.count = self._register_child_endpoint(ProjectProjectsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectProjectsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdEndpoint: The initialized ProjectProjectsIdEndpoint object.
        """
        child = ProjectProjectsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Project]:
        """
        Performs a GET request against the /project/projects endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Project]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Project, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Project]:
        """
        Performs a GET request against the /project/projects endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Project]: The parsed response data.
        """
        return self._parse_many(Project, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Project:
        """
        Performs a POST request against the /project/projects endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Project: The parsed response data.
        """
        return self._parse_one(Project, super()._make_request("POST", data=data, params=params).json())
