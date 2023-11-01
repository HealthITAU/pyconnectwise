from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ScriptsIdCopyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Copy", parent_endpoint=parent_endpoint
        )
