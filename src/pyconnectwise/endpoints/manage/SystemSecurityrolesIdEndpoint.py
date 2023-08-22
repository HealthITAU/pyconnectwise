from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdSettingsEndpoint import SystemSecurityrolesIdSettingsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSecurityrolesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.settings = self._register_child_endpoint(
            SystemSecurityrolesIdSettingsEndpoint(client, parent_endpoint=self)
        )
