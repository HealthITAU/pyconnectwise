from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PluginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Plugins", parent_endpoint=parent_endpoint
        )
