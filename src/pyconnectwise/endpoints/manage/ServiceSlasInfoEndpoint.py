from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasInfoCountEndpoint import (
    ServiceSlasInfoCountEndpoint,
)


class ServiceSlasInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            ServiceSlasInfoCountEndpoint(client, parent_endpoint=self)
        )
