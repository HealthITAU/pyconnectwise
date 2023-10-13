from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdCopyEndpoint import ScheduleCalendarsIdCopyEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdInfoEndpoint import ScheduleCalendarsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdUsagesEndpoint import ScheduleCalendarsIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Calendar
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleCalendarsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Calendar, ConnectWiseManageRequestParams],
    IPatchable[Calendar, ConnectWiseManageRequestParams],
    IPuttable[Calendar, ConnectWiseManageRequestParams],
    IPaginateable[Calendar, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Calendar)
        IPatchable.__init__(self, Calendar)
        IPuttable.__init__(self, Calendar)
        IPaginateable.__init__(self, Calendar)

        self.copy = self._register_child_endpoint(ScheduleCalendarsIdCopyEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(ScheduleCalendarsIdUsagesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ScheduleCalendarsIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Calendar]:
        """
        Performs a GET request against the /schedule/calendars/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Calendar]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Calendar, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Calendar:
        """
        Performs a GET request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Calendar:
        """
        Performs a PATCH request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Calendar:
        """
        Performs a PUT request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("PUT", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
