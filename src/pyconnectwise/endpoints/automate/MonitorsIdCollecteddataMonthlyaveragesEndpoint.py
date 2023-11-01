from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class MonitorsIdCollecteddataMonthlyaveragesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Monthlyaverages", parent_endpoint=parent_endpoint
        )
