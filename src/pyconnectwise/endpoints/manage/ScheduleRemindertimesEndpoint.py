from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleRemindertimesCountEndpoint import ScheduleRemindertimesCountEndpoint
from pyconnectwise.endpoints.manage.ScheduleRemindertimesIdEndpoint import ScheduleRemindertimesIdEndpoint
from pyconnectwise.models.manage import ScheduleReminderTime
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleRemindertimesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reminderTimes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ScheduleRemindertimesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScheduleRemindertimesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleRemindertimesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleRemindertimesIdEndpoint: The initialized ScheduleRemindertimesIdEndpoint object.
        """
        child = ScheduleRemindertimesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ScheduleReminderTime]:
        """
        Performs a GET request against the /schedule/reminderTimes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleReminderTime]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleReminderTime, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleReminderTime]:
        """
        Performs a GET request against the /schedule/reminderTimes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleReminderTime]: The parsed response data.
        """
        return self._parse_many(ScheduleReminderTime, super()._make_request("GET", data=data, params=params).json())
