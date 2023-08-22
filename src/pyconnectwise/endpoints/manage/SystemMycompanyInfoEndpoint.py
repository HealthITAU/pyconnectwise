from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyInfoServicesEndpoint import SystemMycompanyInfoServicesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.services = self._register_child_endpoint(SystemMycompanyInfoServicesEndpoint(client, parent_endpoint=self))
