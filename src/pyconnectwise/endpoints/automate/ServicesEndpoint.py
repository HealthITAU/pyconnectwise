from pyconnectwise.endpoints.automate.ServicesIdEndpoint import ServicesIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ServicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Services", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ServicesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServicesIdEndpoint: The initialized ServicesIdEndpoint object.
        """
        child = ServicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
