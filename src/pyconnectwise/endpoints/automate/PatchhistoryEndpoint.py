from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PatchhistoryEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Patchhistory", parent_endpoint=parent_endpoint
        )
