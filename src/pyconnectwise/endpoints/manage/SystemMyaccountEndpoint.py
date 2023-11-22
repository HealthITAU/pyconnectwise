from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdEndpoint import SystemMyaccountIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMyaccountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "myAccount", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemMyaccountIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyaccountIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemMyaccountIdEndpoint: The initialized SystemMyaccountIdEndpoint object.
        """
        child = SystemMyaccountIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
