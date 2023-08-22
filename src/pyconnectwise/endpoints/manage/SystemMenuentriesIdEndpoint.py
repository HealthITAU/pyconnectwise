from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMenuentriesIdLocationsEndpoint import SystemMenuentriesIdLocationsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMenuentriesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.locations = self._register_child_endpoint(
            SystemMenuentriesIdLocationsEndpoint(client, parent_endpoint=self)
        )
