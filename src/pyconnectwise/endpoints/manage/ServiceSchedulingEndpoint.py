from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSchedulingMembersEndpoint import ServiceSchedulingMembersEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceSchedulingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "scheduling", parent_endpoint=parent_endpoint)

        self.members = self._register_child_endpoint(ServiceSchedulingMembersEndpoint(client, parent_endpoint=self))
