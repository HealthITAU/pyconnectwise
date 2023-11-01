from typing import Any

from pyconnectwise.endpoints.automate.MonitorsIdEndpoint import MonitorsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
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


class MonitorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Monitors", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> MonitorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MonitorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MonitorsIdEndpoint: The initialized MonitorsIdEndpoint object.
        """
        child = MonitorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
