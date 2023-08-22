from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdHolidaysEndpoint import \
    SalesScheduleHolidaylistsIdHolidaysEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesScheduleHolidaylistsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.holidays = self._register_child_endpoint(
            SalesScheduleHolidaylistsIdHolidaysEndpoint(client, parent_endpoint=self)
        )
