from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdSoftwareIdUninstallEndpoint import \
    ComputersIdSoftwareIdUninstallEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdSoftwareIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.uninstall = self._register_child_endpoint(
            ComputersIdSoftwareIdUninstallEndpoint(client, parent_endpoint=self)
        )
