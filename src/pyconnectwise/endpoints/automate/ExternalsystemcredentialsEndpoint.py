from pyconnectwise.endpoints.automate.ExternalsystemcredentialsClientsEndpoint import (
    ExternalsystemcredentialsClientsEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ExternalsystemcredentialsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Externalsystemcredentials", parent_endpoint=parent_endpoint
        )

        self.clients = self._register_child_endpoint(
            ExternalsystemcredentialsClientsEndpoint(client, parent_endpoint=self)
        )
