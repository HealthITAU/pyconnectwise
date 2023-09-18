from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardsEndpoint import ServiceInfoBoardsEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesEndpoint import ServiceInfoBoardtypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.boardtypes = self._register_child_endpoint(ServiceInfoBoardtypesEndpoint(client, parent_endpoint=self))
        self.boards = self._register_child_endpoint(ServiceInfoBoardsEndpoint(client, parent_endpoint=self))
