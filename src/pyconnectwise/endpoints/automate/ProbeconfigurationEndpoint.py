from typing import Any

from pyconnectwise.endpoints.automate.ProbeconfigurationEnableprobeEndpoint import ProbeconfigurationEnableprobeEndpoint
from pyconnectwise.endpoints.automate.ProbeconfigurationIdEndpoint import ProbeconfigurationIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProbeconfigurationEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Probeconfiguration", parent_endpoint=parent_endpoint)

        self.enableprobe = self._register_child_endpoint(
            ProbeconfigurationEnableprobeEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProbeconfigurationIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProbeconfigurationIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProbeconfigurationIdEndpoint: The initialized ProbeconfigurationIdEndpoint object.
        """
        child = ProbeconfigurationIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
