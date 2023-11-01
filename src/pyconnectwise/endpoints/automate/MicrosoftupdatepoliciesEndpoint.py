from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class MicrosoftupdatepoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Microsoftupdatepolicies", parent_endpoint=parent_endpoint
        )
