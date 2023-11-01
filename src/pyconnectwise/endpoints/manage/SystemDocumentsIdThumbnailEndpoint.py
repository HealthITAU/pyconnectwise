from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class SystemDocumentsIdThumbnailEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "thumbnail", parent_endpoint=parent_endpoint
        )
