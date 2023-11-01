from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdHolidaysInfoEndpoint import (
    SalesScheduleHolidaylistsIdHolidaysInfoEndpoint,
)


class SalesScheduleHolidaylistsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "holidays", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            SalesScheduleHolidaylistsIdHolidaysInfoEndpoint(
                client, parent_endpoint=self
            )
        )
