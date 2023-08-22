from typing import Any

from pyconnectwise.endpoints.automate.ServicesIdClassifyEndpoint import ServicesIdClassifyEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.classify = self._register_child_endpoint(ServicesIdClassifyEndpoint(client, parent_endpoint=self))
