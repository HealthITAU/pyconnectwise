from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdEndpoint import SystemMyaccountIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMyaccountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "myAccount", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemMyaccountIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyaccountIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyaccountIdEndpoint: The initialized SystemMyaccountIdEndpoint object.
        """
        child = SystemMyaccountIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
