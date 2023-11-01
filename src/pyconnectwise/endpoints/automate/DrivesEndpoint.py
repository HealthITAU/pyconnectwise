from pyconnectwise.endpoints.automate.DrivesIdEndpoint import DrivesIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class DrivesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Drives", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> DrivesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized DrivesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            DrivesIdEndpoint: The initialized DrivesIdEndpoint object.
        """
        child = DrivesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
