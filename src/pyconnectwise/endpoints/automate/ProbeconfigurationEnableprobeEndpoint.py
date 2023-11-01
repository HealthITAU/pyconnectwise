from pyconnectwise.endpoints.automate.ProbeconfigurationEnableprobeIdEndpoint import (
    ProbeconfigurationEnableprobeIdEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ProbeconfigurationEnableprobeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Enableprobe", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> ProbeconfigurationEnableprobeIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProbeconfigurationEnableprobeIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProbeconfigurationEnableprobeIdEndpoint: The initialized ProbeconfigurationEnableprobeIdEndpoint object.
        """
        child = ProbeconfigurationEnableprobeIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
