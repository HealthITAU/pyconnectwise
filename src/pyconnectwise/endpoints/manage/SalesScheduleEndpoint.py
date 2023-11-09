from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsEndpoint import SalesScheduleHolidaylistsEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "schedule", parent_endpoint=parent_endpoint)

        self.holidaylists = self._register_child_endpoint(
            SalesScheduleHolidaylistsEndpoint(client, parent_endpoint=self)
        )
