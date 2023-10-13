from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamCountEndpoint import SalesOpportunitiesIdTeamCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamIdEndpoint import SalesOpportunitiesIdTeamIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Team
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesOpportunitiesIdTeamEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Team], ConnectWiseManageRequestParams],
    IPostable[Team, ConnectWiseManageRequestParams],
    IPaginateable[Team, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "team", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Team])
        IPostable.__init__(self, Team)
        IPaginateable.__init__(self, Team)

        self.count = self._register_child_endpoint(SalesOpportunitiesIdTeamCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesIdTeamIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdTeamIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdTeamIdEndpoint: The initialized SalesOpportunitiesIdTeamIdEndpoint object.
        """
        child = SalesOpportunitiesIdTeamIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Team]:
        """
        Performs a GET request against the /sales/opportunities/{id}/team endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Team]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Team, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Team]:
        """
        Performs a GET request against the /sales/opportunities/{id}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Team]: The parsed response data.
        """
        return self._parse_many(Team, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Team:
        """
        Performs a POST request against the /sales/opportunities/{id}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Team: The parsed response data.
        """
        return self._parse_one(Team, super()._make_request("POST", data=data, params=params).json())
