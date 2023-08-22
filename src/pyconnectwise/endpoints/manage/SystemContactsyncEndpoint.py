from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringEndpoint import SystemContactsyncMonitoringEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemContactsyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contactsync", parent_endpoint=parent_endpoint)

        self.monitoring = self._register_child_endpoint(
            SystemContactsyncMonitoringEndpoint(client, parent_endpoint=self)
        )
