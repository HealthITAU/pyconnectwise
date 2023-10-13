from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdEndpoint import ProjectBoardsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProjectBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "boards", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ProjectBoardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBoardsIdEndpoint: The initialized ProjectBoardsIdEndpoint object.
        """
        child = ProjectBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
