from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityIdEndpoint import ServicePriorityIdEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityInfoEndpoint import ServicePriorityInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServicePriorityEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "priority", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServicePriorityInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ServicePriorityIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServicePriorityIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServicePriorityIdEndpoint: The initialized ServicePriorityIdEndpoint object.
        """
        child = ServicePriorityIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
