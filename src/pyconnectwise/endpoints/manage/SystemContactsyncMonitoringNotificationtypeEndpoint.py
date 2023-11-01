from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemContactsyncMonitoringNotificationtypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "notificationtype", parent_endpoint=parent_endpoint
        )
