from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBillingratesIdBillingratesIdEndpoint import (
    ProjectBillingratesIdBillingratesIdEndpoint,
)


class ProjectBillingratesIdBillingratesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "billingRates", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ProjectBillingratesIdBillingratesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ProjectBillingratesIdBillingratesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBillingratesIdBillingratesIdEndpoint: The initialized ProjectBillingratesIdBillingratesIdEndpoint object.
        """
        child = ProjectBillingratesIdBillingratesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
