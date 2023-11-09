from pyconnectwise.endpoints.automate.ExternalsystemcredentialsClientsIdEndpoint import (
    ExternalsystemcredentialsClientsIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ExternalsystemcredentialsClientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Clients", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ExternalsystemcredentialsClientsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ExternalsystemcredentialsClientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExternalsystemcredentialsClientsIdEndpoint: The initialized ExternalsystemcredentialsClientsIdEndpoint object.
        """
        child = ExternalsystemcredentialsClientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
