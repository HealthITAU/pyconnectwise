from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsUserdefinedfieldsEventsIdEndpoint import (
    SystemWorkflowsUserdefinedfieldsEventsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemWorkflowsUserdefinedfieldsEventsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "events", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemWorkflowsUserdefinedfieldsEventsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsUserdefinedfieldsEventsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsUserdefinedfieldsEventsIdEndpoint: The initialized SystemWorkflowsUserdefinedfieldsEventsIdEndpoint object.
        """
        child = SystemWorkflowsUserdefinedfieldsEventsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
