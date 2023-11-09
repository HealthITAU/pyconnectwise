from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsIdHolidaysInfoEndpoint import (
    SalesScheduleHolidaylistsIdHolidaysInfoEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesScheduleHolidaylistsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "holidays", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            SalesScheduleHolidaylistsIdHolidaysInfoEndpoint(client, parent_endpoint=self)
        )
