from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesInfoEndpoint import (
    CompanyExpensetypesInfoEndpoint,
)


class CompanyExpensetypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "expenseTypes", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            CompanyExpensetypesInfoEndpoint(client, parent_endpoint=self)
        )
