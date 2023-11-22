from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringEndpoint import (
    SystemContactsyncMonitoringEndpoint,
)


class SystemContactsyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "contactsync", parent_endpoint=parent_endpoint)

        self.monitoring = self._register_child_endpoint(
            SystemContactsyncMonitoringEndpoint(client, parent_endpoint=self)
        )
