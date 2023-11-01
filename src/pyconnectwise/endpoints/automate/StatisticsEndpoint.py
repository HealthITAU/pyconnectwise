from pyconnectwise.endpoints.automate.StatisticsDrivesEndpoint import (
    StatisticsDrivesEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class StatisticsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Statistics", parent_endpoint=parent_endpoint
        )

        self.drives = self._register_child_endpoint(
            StatisticsDrivesEndpoint(client, parent_endpoint=self)
        )
