from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class RebootpoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Rebootpolicies", parent_endpoint=parent_endpoint
        )
