from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemMysecurityCustomizeitemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "customizeItems", parent_endpoint=parent_endpoint
        )
