from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemImportmassmaintenanceIdEndpoint import SystemImportmassmaintenanceIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemImportmassmaintenanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "importMassMaintenance", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemImportmassmaintenanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemImportmassmaintenanceIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemImportmassmaintenanceIdEndpoint: The initialized SystemImportmassmaintenanceIdEndpoint object.
        """
        child = SystemImportmassmaintenanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
