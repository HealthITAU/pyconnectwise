from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyInfoServicesEndpoint import (
    SystemMycompanyInfoServicesEndpoint,
)


class SystemMycompanyInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.services = self._register_child_endpoint(
            SystemMycompanyInfoServicesEndpoint(client, parent_endpoint=self)
        )
