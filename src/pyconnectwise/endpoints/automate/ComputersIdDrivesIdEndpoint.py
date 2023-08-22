from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdDrivesIdSmartdataEndpoint import ComputersIdDrivesIdSmartdataEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdDrivesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.smartdata = self._register_child_endpoint(
            ComputersIdDrivesIdSmartdataEndpoint(client, parent_endpoint=self)
        )
