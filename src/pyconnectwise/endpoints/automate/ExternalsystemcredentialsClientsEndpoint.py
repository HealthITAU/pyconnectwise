from pyconnectwise.endpoints.automate.ExternalsystemcredentialsClientsIdEndpoint import (
    ExternalsystemcredentialsClientsIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ExternalsystemcredentialsClientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Clients", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ExternalsystemcredentialsClientsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExternalsystemcredentialsClientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExternalsystemcredentialsClientsIdEndpoint: The initialized ExternalsystemcredentialsClientsIdEndpoint object.
        """
        child = ExternalsystemcredentialsClientsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
