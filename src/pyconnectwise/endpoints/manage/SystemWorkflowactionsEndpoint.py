from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowactionsIdEndpoint import SystemWorkflowactionsIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowactionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "workflowActions", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemWorkflowactionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowactionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowactionsIdEndpoint: The initialized SystemWorkflowactionsIdEndpoint object.
        """
        child = SystemWorkflowactionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
