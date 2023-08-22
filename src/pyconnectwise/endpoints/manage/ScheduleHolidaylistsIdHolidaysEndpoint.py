from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysIdEndpoint import \
    ScheduleHolidaylistsIdHolidaysIdEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysInfoEndpoint import \
    ScheduleHolidaylistsIdHolidaysInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleHolidaylistsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidays", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ScheduleHolidaylistsIdHolidaysInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScheduleHolidaylistsIdHolidaysIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScheduleHolidaylistsIdHolidaysIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleHolidaylistsIdHolidaysIdEndpoint: The initialized ScheduleHolidaylistsIdHolidaysIdEndpoint object.
        """
        child = ScheduleHolidaylistsIdHolidaysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
