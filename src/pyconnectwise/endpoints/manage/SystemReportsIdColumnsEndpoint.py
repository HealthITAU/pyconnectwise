from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemReportsIdColumnsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "columns", parent_endpoint=parent_endpoint
        )
