from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesEndpoint import FinanceAccountingBatchesEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingExportEndpoint import FinanceAccountingExportEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesEndpoint import \
    FinanceAccountingUnpostedexpensesEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesEndpoint import \
    FinanceAccountingUnpostedinvoicesEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementEndpoint import \
    FinanceAccountingUnpostedprocurementEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accounting", parent_endpoint=parent_endpoint)

        self.export = self._register_child_endpoint(FinanceAccountingExportEndpoint(client, parent_endpoint=self))
        self.batches = self._register_child_endpoint(FinanceAccountingBatchesEndpoint(client, parent_endpoint=self))
        self.unpostedexpenses = self._register_child_endpoint(
            FinanceAccountingUnpostedexpensesEndpoint(client, parent_endpoint=self)
        )
        self.unpostedprocurement = self._register_child_endpoint(
            FinanceAccountingUnpostedprocurementEndpoint(client, parent_endpoint=self)
        )
        self.unpostedinvoices = self._register_child_endpoint(
            FinanceAccountingUnpostedinvoicesEndpoint(client, parent_endpoint=self)
        )
