from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesServicePriorityEndpoint import (
    SalesServicePriorityEndpoint,
)


class SalesServiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "service", parent_endpoint=parent_endpoint
        )

        self.priority = self._register_child_endpoint(
            SalesServicePriorityEndpoint(client, parent_endpoint=self)
        )
