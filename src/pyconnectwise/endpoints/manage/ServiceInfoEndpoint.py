from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardsEndpoint import ServiceInfoBoardsEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesEndpoint import ServiceInfoBoardtypesEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)

        self.boards = self._register_child_endpoint(ServiceInfoBoardsEndpoint(client, parent_endpoint=self))
        self.boardtypes = self._register_child_endpoint(ServiceInfoBoardtypesEndpoint(client, parent_endpoint=self))
