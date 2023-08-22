from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBillingratesIdBillingratesIdEndpoint import \
    ProjectBillingratesIdBillingratesIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectBillingratesIdBillingratesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingRates", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ProjectBillingratesIdBillingratesIdEndpoint:
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
