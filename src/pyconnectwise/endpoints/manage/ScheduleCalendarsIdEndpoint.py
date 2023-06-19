from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdCopyEndpoint import ScheduleCalendarsIdCopyEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdInfoEndpoint import ScheduleCalendarsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ScheduleCalendarsIdUsagesEndpoint import ScheduleCalendarsIdUsagesEndpoint
from pyconnectwise.models.manage.CalendarModel import CalendarModel

class ScheduleCalendarsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            ScheduleCalendarsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ScheduleCalendarsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            ScheduleCalendarsIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CalendarModel]:
        """
        Performs a GET request against the /schedule/calendars/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CalendarModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CalendarModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CalendarModel:
        """
        Performs a GET request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CalendarModel: The parsed response data.
        """
        return self._parse_one(CalendarModel, super().make_request("GET", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CalendarModel:
        """
        Performs a PATCH request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CalendarModel: The parsed response data.
        """
        return self._parse_one(CalendarModel, super().make_request("PATCH", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CalendarModel:
        """
        Performs a PUT request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CalendarModel: The parsed response data.
        """
        return self._parse_one(CalendarModel, super().make_request("PUT", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /schedule/calendars/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        