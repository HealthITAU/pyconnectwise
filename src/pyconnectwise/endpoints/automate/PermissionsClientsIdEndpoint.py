from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PermissionsClientsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
