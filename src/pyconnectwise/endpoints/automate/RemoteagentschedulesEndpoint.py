from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechRemoteAgentSchedule
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class RemoteagentschedulesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechRemoteAgentSchedule], ConnectWiseAutomateRequestParams],
    IPostable[LabTechRemoteAgentSchedule, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechRemoteAgentSchedule, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Remoteagentschedules", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechRemoteAgentSchedule])
        IPostable.__init__(self, LabTechRemoteAgentSchedule)
        IPaginateable.__init__(self, LabTechRemoteAgentSchedule)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechRemoteAgentSchedule]:
        """
        Performs a GET request against the /Remoteagentschedules endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechRemoteAgentSchedule]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechRemoteAgentSchedule,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechRemoteAgentSchedule]:
        """
        Performs a GET request against the /Remoteagentschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechRemoteAgentSchedule]: The parsed response data.
        """
        return self._parse_many(
            LabTechRemoteAgentSchedule,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechRemoteAgentSchedule:
        """
        Performs a POST request against the /Remoteagentschedules endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechRemoteAgentSchedule: The parsed response data.
        """
        return self._parse_one(
            LabTechRemoteAgentSchedule,
            super()._make_request("POST", data=data, params=params).json(),
        )
