from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ScheduleReminderTimesIdEndpoint import ScheduleReminderTimesIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleReminderTimesCountEndpoint import ScheduleReminderTimesCountEndpoint
from pyconnectwise.models.manage.ScheduleReminderTimeModel import ScheduleReminderTimeModel

class ScheduleReminderTimesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reminderTimes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleReminderTimesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ScheduleReminderTimesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleReminderTimesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleReminderTimesIdEndpoint: The initialized ScheduleReminderTimesIdEndpoint object.
        """
        child = ScheduleReminderTimesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ScheduleReminderTimeModel]:
        """
        Performs a GET request against the /schedule/reminderTimes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleReminderTimeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ScheduleReminderTimeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleReminderTimeModel]:
        """
        Performs a GET request against the /schedule/reminderTimes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleReminderTimeModel]: The parsed response data.
        """
        return self._parse_many(ScheduleReminderTimeModel, super().make_request("GET", params=params).json())
        