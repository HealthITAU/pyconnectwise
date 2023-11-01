from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdPatchjobsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Patchjobs", parent_endpoint=parent_endpoint
        )
