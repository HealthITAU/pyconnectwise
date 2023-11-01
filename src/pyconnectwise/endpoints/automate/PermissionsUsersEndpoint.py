from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PermissionsUsersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Users", parent_endpoint=parent_endpoint
        )
