from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdHolidaysInfoCountEndpoint import (
    SalesScheduleHolidaylistsIdHolidaysInfoCountEndpoint,
)


class SalesScheduleHolidaylistsIdHolidaysInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            SalesScheduleHolidaylistsIdHolidaysInfoCountEndpoint(
                client, parent_endpoint=self
            )
        )
