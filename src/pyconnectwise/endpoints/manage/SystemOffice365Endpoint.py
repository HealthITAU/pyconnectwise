from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailsetupsEndpoint import SystemOffice365EmailsetupsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemOffice365Endpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "office365", parent_endpoint=parent_endpoint)

        self.email_setups = self._register_child_endpoint(
            SystemOffice365EmailsetupsEndpoint(client, parent_endpoint=self)
        )
