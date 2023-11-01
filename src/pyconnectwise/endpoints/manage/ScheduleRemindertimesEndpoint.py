from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleRemindertimesCountEndpoint import (
    ScheduleRemindertimesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleRemindertimesIdEndpoint import (
    ScheduleRemindertimesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ScheduleReminderTime
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ScheduleRemindertimesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleReminderTime], ConnectWiseManageRequestParams],
    IPaginateable[ScheduleReminderTime, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "reminderTimes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleReminderTime])
        IPaginateable.__init__(self, ScheduleReminderTime)

        self.count = self._register_child_endpoint(
            ScheduleRemindertimesCountEndpoint(client, parent_endpoint=self)
        )

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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleReminderTime,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleReminderTime]:
        """
        Performs a GET request against the /schedule/reminderTimes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleReminderTime]: The parsed response data.
        """
        return self._parse_many(
            ScheduleReminderTime,
            super()._make_request("GET", data=data, params=params).json(),
        )
