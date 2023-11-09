from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMarketplaceimportGetdefinitionIdEndpoint import (
    SystemMarketplaceimportGetdefinitionIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMarketplaceimportGetdefinitionEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "getdefinition", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemMarketplaceimportGetdefinitionIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMarketplaceimportGetdefinitionIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemMarketplaceimportGetdefinitionIdEndpoint: The initialized SystemMarketplaceimportGetdefinitionIdEndpoint object.
        """
        child = SystemMarketplaceimportGetdefinitionIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
