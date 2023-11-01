from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class MonitorstatisticsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Monitorstatistics", parent_endpoint=parent_endpoint
        )
