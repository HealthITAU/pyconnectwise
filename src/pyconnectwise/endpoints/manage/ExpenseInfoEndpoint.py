from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoTaxtypesEndpoint import (
    ExpenseInfoTaxtypesEndpoint,
)


class ExpenseInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.tax_types = self._register_child_endpoint(
            ExpenseInfoTaxtypesEndpoint(client, parent_endpoint=self)
        )
