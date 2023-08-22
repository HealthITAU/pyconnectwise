from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesServicePriorityEndpoint import SalesServicePriorityEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesServiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "service", parent_endpoint=parent_endpoint)

        self.priority = self._register_child_endpoint(SalesServicePriorityEndpoint(client, parent_endpoint=self))
