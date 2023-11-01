from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDirectionalsyncsIdInfoEndpoint import (
    SystemDirectionalsyncsIdInfoEndpoint,
)


class SystemDirectionalsyncsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            SystemDirectionalsyncsIdInfoEndpoint(client, parent_endpoint=self)
        )
