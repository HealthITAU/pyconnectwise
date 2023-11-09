from pyconnectwise.endpoints.automate.ServicesIdClassifyEndpoint import (
    ServicesIdClassifyEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ServicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.classify = self._register_child_endpoint(ServicesIdClassifyEndpoint(client, parent_endpoint=self))
