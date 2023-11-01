from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesEndpoint import (
    FinanceAccountingBatchesEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingExportEndpoint import (
    FinanceAccountingExportEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesEndpoint import (
    FinanceAccountingUnpostedexpensesEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesEndpoint import (
    FinanceAccountingUnpostedinvoicesEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementEndpoint import (
    FinanceAccountingUnpostedprocurementEndpoint,
)


class FinanceAccountingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "accounting", parent_endpoint=parent_endpoint
        )

        self.unpostedinvoices = self._register_child_endpoint(
            FinanceAccountingUnpostedinvoicesEndpoint(client, parent_endpoint=self)
        )
        self.unpostedprocurement = self._register_child_endpoint(
            FinanceAccountingUnpostedprocurementEndpoint(client, parent_endpoint=self)
        )
        self.unpostedexpenses = self._register_child_endpoint(
            FinanceAccountingUnpostedexpensesEndpoint(client, parent_endpoint=self)
        )
        self.batches = self._register_child_endpoint(
            FinanceAccountingBatchesEndpoint(client, parent_endpoint=self)
        )
        self.export = self._register_child_endpoint(
            FinanceAccountingExportEndpoint(client, parent_endpoint=self)
        )
