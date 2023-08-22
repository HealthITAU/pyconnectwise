from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBillingratesIdEndpoint import ProjectBillingratesIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectBillingratesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingRates", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ProjectBillingratesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBillingratesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBillingratesIdEndpoint: The initialized ProjectBillingratesIdEndpoint object.
        """
        child = ProjectBillingratesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
