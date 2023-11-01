from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMarketplaceimportGetdefinitionEndpoint import (
    SystemMarketplaceimportGetdefinitionEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMarketplaceimportImportEndpoint import (
    SystemMarketplaceimportImportEndpoint,
)


class SystemMarketplaceimportEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "marketplaceimport", parent_endpoint=parent_endpoint
        )

        self.import_ = self._register_child_endpoint(
            SystemMarketplaceimportImportEndpoint(client, parent_endpoint=self)
        )
        self.getdefinition = self._register_child_endpoint(
            SystemMarketplaceimportGetdefinitionEndpoint(client, parent_endpoint=self)
        )
