from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectTicketnoteIdEndpoint import ProjectTicketnoteIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProjectTicketnoteEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "ticketNote", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> ProjectTicketnoteIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectTicketnoteIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProjectTicketnoteIdEndpoint: The initialized ProjectTicketnoteIdEndpoint object.
        """
        child = ProjectTicketnoteIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
