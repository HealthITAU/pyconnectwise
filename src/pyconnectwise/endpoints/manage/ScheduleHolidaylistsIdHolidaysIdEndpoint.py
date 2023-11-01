from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysIdInfoEndpoint import (
    ScheduleHolidaylistsIdHolidaysIdInfoEndpoint,
)


class ScheduleHolidaylistsIdHolidaysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            ScheduleHolidaylistsIdHolidaysIdInfoEndpoint(client, parent_endpoint=self)
        )
