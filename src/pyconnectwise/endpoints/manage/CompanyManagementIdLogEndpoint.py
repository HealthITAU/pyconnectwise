from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdLogDownloadEndpoint import CompanyManagementIdLogDownloadEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyManagementIdLogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "log", parent_endpoint=parent_endpoint)

        self.download = self._register_child_endpoint(
            CompanyManagementIdLogDownloadEndpoint(client, parent_endpoint=self)
        )
