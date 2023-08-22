from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTeamsIdUsagesListEndpoint import \
    ServiceBoardsIdTeamsIdUsagesListEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceBoardsIdTeamsIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "usages", parent_endpoint=parent_endpoint)

        self.list = self._register_child_endpoint(
            ServiceBoardsIdTeamsIdUsagesListEndpoint(client, parent_endpoint=self)
        )
