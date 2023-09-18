from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsCountEndpoint import ScheduleCalendarsCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdEndpoint import ScheduleCalendarsIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsInfoEndpoint import ScheduleCalendarsInfoEndpoint
from pyconnectwise.models.manage import Calendar
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleCalendarsEndpoint(ConnectWiseEndpoint):
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

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Calendar]:
        """
        Performs a GET request against the /schedule/calendars endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Calendar]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Calendar, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Calendar]:
        """
        Performs a GET request against the /schedule/calendars endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Calendar]: The parsed response data.
        """
        return self._parse_many(Calendar, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Calendar:
        """
        Performs a POST request against the /schedule/calendars endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Calendar: The parsed response data.
        """
        return self._parse_one(Calendar, super()._make_request("POST", data=data, params=params).json())
