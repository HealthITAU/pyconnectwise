from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import TeamMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceTeammembersEndpoint(ConnectWiseEndpoint, IPostable[TeamMember, ConnectWiseManageRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "teamMembers", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, TeamMember)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> TeamMember:
        """
        Performs a POST request against the /service/teamMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TeamMember: The parsed response data.
        """
        return self._parse_one(TeamMember, super()._make_request("POST", data=data, params=params).json())
