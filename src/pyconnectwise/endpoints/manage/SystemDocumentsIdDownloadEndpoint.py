from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemDocumentsIdDownloadEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "download", parent_endpoint=parent_endpoint
        )
