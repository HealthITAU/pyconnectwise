from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesScheduleHolidaylistsEndpoint import SalesScheduleHolidaylistsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesScheduleEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "schedule", parent_endpoint=parent_endpoint)

        self.holidaylists = self._register_child_endpoint(
            SalesScheduleHolidaylistsEndpoint(client, parent_endpoint=self)
        )
