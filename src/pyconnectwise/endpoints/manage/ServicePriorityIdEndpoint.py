from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePriorityIdInfoEndpoint import (
    ServicePriorityIdInfoEndpoint,
)


class ServicePriorityIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            ServicePriorityIdInfoEndpoint(client, parent_endpoint=self)
        )
