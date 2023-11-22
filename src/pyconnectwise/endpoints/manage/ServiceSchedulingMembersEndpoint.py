from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingMembersIdEndpoint import ServiceSchedulingMembersIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingMembersInfoEndpoint import ServiceSchedulingMembersInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceSchedulingMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "members", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ServiceSchedulingMembersInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ServiceSchedulingMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSchedulingMembersIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServiceSchedulingMembersIdEndpoint: The initialized ServiceSchedulingMembersIdEndpoint object.
        """
        child = ServiceSchedulingMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
