from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsActionsEndpoint import \
    SystemWorkflowsUserdefinedfieldsActionsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsEndpoint import \
    SystemWorkflowsUserdefinedfieldsEventsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsIdEndpoint import \
    SystemWorkflowsUserdefinedfieldsIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemWorkflowsUserdefinedfieldsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "userdefinedfields", parent_endpoint=parent_endpoint)

        self.actions = self._register_child_endpoint(
            SystemWorkflowsUserdefinedfieldsActionsEndpoint(client, parent_endpoint=self)
        )
        self.events = self._register_child_endpoint(
            SystemWorkflowsUserdefinedfieldsEventsEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemWorkflowsUserdefinedfieldsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
