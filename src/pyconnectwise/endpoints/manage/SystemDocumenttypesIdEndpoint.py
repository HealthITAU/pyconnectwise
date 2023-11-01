from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDocumenttypesIdInfoEndpoint import (
    SystemDocumenttypesIdInfoEndpoint,
)


class SystemDocumenttypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            SystemDocumenttypesIdInfoEndpoint(client, parent_endpoint=self)
        )
