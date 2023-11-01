from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ProjectTicketnoteIdMarkasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "markAs", parent_endpoint=parent_endpoint
        )
