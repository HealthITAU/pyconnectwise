from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteIdEndpoint import (
    ProjectTicketnoteIdEndpoint,
)


class ProjectTicketnoteEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "ticketNote", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ProjectTicketnoteIdEndpoint:  # noqa: A002
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
