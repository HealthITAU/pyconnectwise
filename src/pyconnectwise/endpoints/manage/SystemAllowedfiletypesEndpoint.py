from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedfiletypesCountEndpoint import SystemAllowedfiletypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedfiletypesIdEndpoint import SystemAllowedfiletypesIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemAllowedfiletypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "allowedfiletypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemAllowedfiletypesCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemAllowedfiletypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemAllowedfiletypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemAllowedfiletypesIdEndpoint: The initialized SystemAllowedfiletypesIdEndpoint object.
        """
        child = SystemAllowedfiletypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
