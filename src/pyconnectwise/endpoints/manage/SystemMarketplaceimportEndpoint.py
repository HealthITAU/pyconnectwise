from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMarketplaceimportGetdefinitionEndpoint import (
    SystemMarketplaceimportGetdefinitionEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMarketplaceimportImportEndpoint import SystemMarketplaceimportImportEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMarketplaceimportEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "marketplaceimport", parent_endpoint=parent_endpoint)

        self.import_ = self._register_child_endpoint(
            SystemMarketplaceimportImportEndpoint(client, parent_endpoint=self)
        )
        self.getdefinition = self._register_child_endpoint(
            SystemMarketplaceimportGetdefinitionEndpoint(client, parent_endpoint=self)
        )
