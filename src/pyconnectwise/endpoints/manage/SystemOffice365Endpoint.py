from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailsetupsEndpoint import SystemOffice365EmailsetupsEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemOffice365Endpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "office365", parent_endpoint=parent_endpoint)

        self.email_setups = self._register_child_endpoint(
            SystemOffice365EmailsetupsEndpoint(client, parent_endpoint=self)
        )
