from pyconnectwise.endpoints.automate.ComputersIdDrivesIdEndpoint import (
    ComputersIdDrivesIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ComputersIdDrivesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Drives", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ComputersIdDrivesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ComputersIdDrivesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ComputersIdDrivesIdEndpoint: The initialized ComputersIdDrivesIdEndpoint object.
        """
        child = ComputersIdDrivesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
