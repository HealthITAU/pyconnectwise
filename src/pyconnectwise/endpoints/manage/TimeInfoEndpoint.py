from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeInfoChargecodeexpensetypesEndpoint import (
    TimeInfoChargecodeexpensetypesEndpoint,
)


class TimeInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.charge_code_expense_types = self._register_child_endpoint(
            TimeInfoChargecodeexpensetypesEndpoint(client, parent_endpoint=self)
        )
