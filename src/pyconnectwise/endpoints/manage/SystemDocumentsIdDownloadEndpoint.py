from requests import Response
from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemDocumentsIdDownloadEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "download", parent_endpoint=parent_endpoint)

    def stream(self) -> Response:
        """
        Performs a GET request against the /system/documents/{id}/download endpoint and returns the response object, supporting streaming
        """
        return super()._make_request("GET", stream=True)
