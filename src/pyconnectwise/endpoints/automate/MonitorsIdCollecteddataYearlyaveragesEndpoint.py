from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class MonitorsIdCollecteddataYearlyaveragesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Yearlyaverages", parent_endpoint=parent_endpoint
        )
