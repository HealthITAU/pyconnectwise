from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsCountEndpoint import ScheduleCalendarsCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdEndpoint import ScheduleCalendarsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsInfoEndpoint import ScheduleCalendarsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Calendar
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleCalendarsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Calendar], ConnectWiseManageRequestParams],
    IPostable[Calendar, ConnectWiseManageRequestParams],
    IPaginateable[Calendar, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "calendars", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ScheduleCalendarsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ScheduleCalendarsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScheduleCalendarsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleCalendarsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleCalendarsIdEndpoint: The initialized ScheduleCalendarsIdEndpoint object.
        """
        child = ScheduleCalendarsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Calendar]:
        """
        Performs a GET request against the /schedule/calendars endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Calendar]:
        """
        Performs a GET request against the /schedule/calendars endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Calendar]: The parsed response data.
        """
        return self._parse_many(Calendar, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Calendar:
        """
        Performs a POST request against the /schedule/calendars endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("POST", data=data, params=params).json())
