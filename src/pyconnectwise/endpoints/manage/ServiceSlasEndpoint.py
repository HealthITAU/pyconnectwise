from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdEndpoint import ServiceSlasIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasInfoEndpoint import ServiceSlasInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSlasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "slas", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServiceSlasInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceSlasIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSlasIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSlasIdEndpoint: The initialized ServiceSlasIdEndpoint object.
        """
        child = ServiceSlasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
