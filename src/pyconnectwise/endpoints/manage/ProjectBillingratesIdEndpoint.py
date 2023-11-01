from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectBillingratesIdBillingratesEndpoint import (
    ProjectBillingratesIdBillingratesEndpoint,
)


class ProjectBillingratesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.billing_rates = self._register_child_endpoint(
            ProjectBillingratesIdBillingratesEndpoint(client, parent_endpoint=self)
        )
