from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemWorkflowsIdEventsIdTestEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "test", parent_endpoint=parent_endpoint
        )
