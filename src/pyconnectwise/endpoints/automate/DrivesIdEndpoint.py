from typing import Any

from pyconnectwise.endpoints.automate.DrivesIdDrivestatsEndpoint import DrivesIdDrivestatsEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class DrivesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.drivestats = self._register_child_endpoint(DrivesIdDrivestatsEndpoint(client, parent_endpoint=self))
