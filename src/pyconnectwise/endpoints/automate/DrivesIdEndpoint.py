from pyconnectwise.endpoints.automate.DrivesIdDrivestatsEndpoint import (
    DrivesIdDrivestatsEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class DrivesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.drivestats = self._register_child_endpoint(
            DrivesIdDrivestatsEndpoint(client, parent_endpoint=self)
        )
