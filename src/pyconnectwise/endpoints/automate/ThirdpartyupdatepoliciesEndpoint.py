from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ThirdpartyupdatepoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Thirdpartyupdatepolicies", parent_endpoint=parent_endpoint)
