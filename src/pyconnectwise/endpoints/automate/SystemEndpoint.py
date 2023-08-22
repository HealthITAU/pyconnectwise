from typing import Any

from pyconnectwise.endpoints.automate.SystemServerinformationEndpoint import SystemServerinformationEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "System", parent_endpoint=parent_endpoint)

        self.serverinformation = self._register_child_endpoint(
            SystemServerinformationEndpoint(client, parent_endpoint=self)
        )
