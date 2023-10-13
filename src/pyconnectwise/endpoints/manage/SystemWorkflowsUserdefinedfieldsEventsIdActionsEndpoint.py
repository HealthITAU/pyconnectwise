from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint import \
    SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemWorkflowsUserdefinedfieldsEventsIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "actions", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsEventsIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
