from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMarketplaceimportGetdefinitionIdEndpoint import (
    SystemMarketplaceimportGetdefinitionIdEndpoint,
)


class SystemMarketplaceimportGetdefinitionEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "getdefinition", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemMarketplaceimportGetdefinitionIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMarketplaceimportGetdefinitionIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMarketplaceimportGetdefinitionIdEndpoint: The initialized SystemMarketplaceimportGetdefinitionIdEndpoint object.
        """
        child = SystemMarketplaceimportGetdefinitionIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
