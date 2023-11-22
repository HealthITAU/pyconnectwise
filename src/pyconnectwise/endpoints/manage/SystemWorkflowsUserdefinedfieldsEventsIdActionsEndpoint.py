from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint import (
    SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "actions", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
