from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesServicePriorityInfoEndpoint import SalesServicePriorityInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesServicePriorityEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "priority", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesServicePriorityInfoEndpoint(client, parent_endpoint=self))
