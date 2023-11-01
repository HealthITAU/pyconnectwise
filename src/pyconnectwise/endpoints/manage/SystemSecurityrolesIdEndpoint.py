from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdSettingsEndpoint import (
    SystemSecurityrolesIdSettingsEndpoint,
)


class SystemSecurityrolesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.settings = self._register_child_endpoint(
            SystemSecurityrolesIdSettingsEndpoint(client, parent_endpoint=self)
        )
