from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdEndpoint import (
    SystemWorkflowsUserdefinedfieldsEventsIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemWorkflowsUserdefinedfieldsEventsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "events", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SystemWorkflowsUserdefinedfieldsEventsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsEventsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsEventsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsEventsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsEventsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
