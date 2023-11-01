from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdInfoEndpoint import (
    ServiceSlasIdInfoEndpoint,
)


class ServiceSlasIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            ServiceSlasIdInfoEndpoint(client, parent_endpoint=self)
        )
