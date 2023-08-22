from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsActionsIdEndpoint import \
    SystemWorkflowsUserdefinedfieldsActionsIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsUserdefinedfieldsActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "actions", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemWorkflowsUserdefinedfieldsActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsActionsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsActionsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
