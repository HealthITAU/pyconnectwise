from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemAllowedfiletypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "AllowedFileTypes", parent_endpoint=parent_endpoint
        )
