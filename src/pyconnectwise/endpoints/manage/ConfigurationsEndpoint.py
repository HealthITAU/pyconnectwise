from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint

class ConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "configurations")
        