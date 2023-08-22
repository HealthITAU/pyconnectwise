from typing import Any

from pyconnectwise.endpoints.automate.StatisticsDrivesEndpoint import StatisticsDrivesEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class StatisticsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Statistics", parent_endpoint=parent_endpoint)

        self.drives = self._register_child_endpoint(StatisticsDrivesEndpoint(client, parent_endpoint=self))
