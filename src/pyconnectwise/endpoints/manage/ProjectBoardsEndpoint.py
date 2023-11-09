from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdEndpoint import ProjectBoardsIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProjectBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "boards", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> ProjectBoardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProjectBoardsIdEndpoint: The initialized ProjectBoardsIdEndpoint object.
        """
        child = ProjectBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
