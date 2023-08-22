from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProjectIdBillingratesEndpoint import ProjectIdBillingratesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProjectIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.billing_rates = self._register_child_endpoint(ProjectIdBillingratesEndpoint(client, parent_endpoint=self))
