from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdAlertsuspensionsTemplatediversionEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Templatediversion", parent_endpoint=parent_endpoint
        )
