from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsEndpoint import (
    SalesScheduleHolidaylistsEndpoint,
)


class SalesScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "schedule", parent_endpoint=parent_endpoint
        )

        self.holidaylists = self._register_child_endpoint(
            SalesScheduleHolidaylistsEndpoint(client, parent_endpoint=self)
        )
