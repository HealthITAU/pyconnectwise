from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdEndpoint import ConfigurationsTypesIdEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesInfoEndpoint import ConfigurationsTypesInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ConfigurationsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ConfigurationsTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ConfigurationsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ConfigurationsTypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ConfigurationsTypesIdEndpoint: The initialized ConfigurationsTypesIdEndpoint object.
        """
        child = ConfigurationsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
