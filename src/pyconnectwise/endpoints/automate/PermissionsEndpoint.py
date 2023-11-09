from pyconnectwise.endpoints.automate.PermissionsClientsEndpoint import (
    PermissionsClientsEndpoint,
)
from pyconnectwise.endpoints.automate.PermissionsUsersEndpoint import (
    PermissionsUsersEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PermissionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Permissions", parent_endpoint=parent_endpoint)

        self.clients = self._register_child_endpoint(PermissionsClientsEndpoint(client, parent_endpoint=self))
        self.users = self._register_child_endpoint(PermissionsUsersEndpoint(client, parent_endpoint=self))
