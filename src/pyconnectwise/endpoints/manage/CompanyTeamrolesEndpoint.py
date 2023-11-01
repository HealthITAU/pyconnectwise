from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyTeamrolesCountEndpoint import (
    CompanyTeamrolesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyTeamrolesIdEndpoint import (
    CompanyTeamrolesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyTeamrolesInfoEndpoint import (
    CompanyTeamrolesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import TeamRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyTeamrolesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TeamRole], ConnectWiseManageRequestParams],
    IPostable[TeamRole, ConnectWiseManageRequestParams],
    IPaginateable[TeamRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "teamRoles", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TeamRole])
        IPostable.__init__(self, TeamRole)
        IPaginateable.__init__(self, TeamRole)

        self.count = self._register_child_endpoint(
            CompanyTeamrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyTeamrolesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyTeamrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTeamrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyTeamrolesIdEndpoint: The initialized CompanyTeamrolesIdEndpoint object.
        """
        child = CompanyTeamrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TeamRole]:
        """
        Performs a GET request against the /company/teamRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TeamRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TeamRole,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TeamRole]:
        """
        Performs a GET request against the /company/teamRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TeamRole]: The parsed response data.
        """
        return self._parse_many(
            TeamRole, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TeamRole:
        """
        Performs a POST request against the /company/teamRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TeamRole: The parsed response data.
        """
        return self._parse_one(
            TeamRole, super()._make_request("POST", data=data, params=params).json()
        )
