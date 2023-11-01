from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdEndpoint import (
    ProjectBoardsIdEndpoint,
)


class ProjectBoardsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "boards", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ProjectBoardsIdEndpoint:  # noqa: A002
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
