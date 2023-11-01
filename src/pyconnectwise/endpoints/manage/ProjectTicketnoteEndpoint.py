from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteIdEndpoint import (
    ProjectTicketnoteIdEndpoint,
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


class ProjectTicketnoteEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "ticketNote", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ProjectTicketnoteIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketnoteIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectTicketnoteIdEndpoint: The initialized ProjectTicketnoteIdEndpoint object.
        """
        child = ProjectTicketnoteIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
