from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdAlertsuspensionsMaintenancewindowEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Maintenancewindow", parent_endpoint=parent_endpoint
        )
