from pyconnectwise.endpoints.automate.SystemServerinformationEndpoint import (
    SystemServerinformationEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "System", parent_endpoint=parent_endpoint
        )

        self.serverinformation = self._register_child_endpoint(
            SystemServerinformationEndpoint(client, parent_endpoint=self)
        )
