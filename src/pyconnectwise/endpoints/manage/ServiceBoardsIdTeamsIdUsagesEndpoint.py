from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsIdUsagesListEndpoint import (
    ServiceBoardsIdTeamsIdUsagesListEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceBoardsIdTeamsIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "usages", parent_endpoint=parent_endpoint)

        self.list = self._register_child_endpoint(
            ServiceBoardsIdTeamsIdUsagesListEndpoint(client, parent_endpoint=self)
        )
