from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Calendar
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleCalendarsIdCopyEndpoint(ConnectWiseEndpoint, IPostable[Calendar, ConnectWiseManageRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "copy", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Calendar)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Calendar:
        """
        Performs a POST request against the /schedule/calendars/{id}/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("POST", data=data, params=params).json())
