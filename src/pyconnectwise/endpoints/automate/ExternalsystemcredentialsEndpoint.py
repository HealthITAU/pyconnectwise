from typing import Any

from pyconnectwise.endpoints.automate.ExternalsystemcredentialsClientsEndpoint import \
    ExternalsystemcredentialsClientsEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExternalsystemcredentialsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Externalsystemcredentials", parent_endpoint=parent_endpoint)

        self.clients = self._register_child_endpoint(
            ExternalsystemcredentialsClientsEndpoint(client, parent_endpoint=self)
        )
