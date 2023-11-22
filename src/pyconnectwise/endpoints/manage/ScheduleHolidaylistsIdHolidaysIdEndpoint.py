from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysIdInfoEndpoint import (
    ScheduleHolidaylistsIdHolidaysIdInfoEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ScheduleHolidaylistsIdHolidaysIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ScheduleHolidaylistsIdHolidaysIdInfoEndpoint(client, parent_endpoint=self)
        )
