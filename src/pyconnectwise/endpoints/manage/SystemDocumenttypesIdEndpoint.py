from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDocumenttypesIdInfoEndpoint import SystemDocumenttypesIdInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemDocumenttypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemDocumenttypesIdInfoEndpoint(client, parent_endpoint=self))
