from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesCountEndpoint import ProjectSecurityrolesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityrolesIdEndpoint import ProjectSecurityrolesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProjectSecurityRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectSecurityrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProjectSecurityRole], ConnectWiseManageRequestParams],
    IPostable[ProjectSecurityRole, ConnectWiseManageRequestParams],
    IPaginateable[ProjectSecurityRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "securityRoles", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProjectSecurityrolesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProjectSecurityrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectSecurityrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectSecurityrolesIdEndpoint: The initialized ProjectSecurityrolesIdEndpoint object.
        """
        child = ProjectSecurityrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProjectSecurityRole]:
        """
        Performs a GET request against the /project/securityRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectSecurityRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProjectSecurityRole, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProjectSecurityRole]:
        """
        Performs a GET request against the /project/securityRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectSecurityRole]: The parsed response data.
        """
        return self._parse_many(ProjectSecurityRole, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProjectSecurityRole:
        """
        Performs a POST request against the /project/securityRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectSecurityRole: The parsed response data.
        """
        return self._parse_one(ProjectSecurityRole, super()._make_request("POST", data=data, params=params).json())
