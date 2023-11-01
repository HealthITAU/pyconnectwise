from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdThirdpartypatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Thirdpartypatches", parent_endpoint=parent_endpoint
        )
