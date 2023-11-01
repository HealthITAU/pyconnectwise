from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesIdLocationsEndpoint import (
    SystemMenuentriesIdLocationsEndpoint,
)


class SystemMenuentriesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.locations = self._register_child_endpoint(
            SystemMenuentriesIdLocationsEndpoint(client, parent_endpoint=self)
        )
