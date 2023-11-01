from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesEndpoint import (
    ConfigurationsTypesEndpoint,
)


class ConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "configurations", parent_endpoint=parent_endpoint
        )

        self.types = self._register_child_endpoint(
            ConfigurationsTypesEndpoint(client, parent_endpoint=self)
        )
