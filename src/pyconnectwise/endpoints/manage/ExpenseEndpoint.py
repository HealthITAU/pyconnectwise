from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseClassificationsEndpoint import ExpenseClassificationsEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesEndpoint import ExpenseEntriesEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoEndpoint import ExpenseInfoEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesEndpoint import ExpensePaymenttypesEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsEndpoint import ExpenseReportsEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesEndpoint import ExpenseTypesEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "expense", parent_endpoint=parent_endpoint)

        self.classifications = self._register_child_endpoint(
            ExpenseClassificationsEndpoint(client, parent_endpoint=self)
        )
        self.reports = self._register_child_endpoint(ExpenseReportsEndpoint(client, parent_endpoint=self))
        self.payment_types = self._register_child_endpoint(ExpensePaymenttypesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(ExpenseTypesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ExpenseInfoEndpoint(client, parent_endpoint=self))
        self.entries = self._register_child_endpoint(ExpenseEntriesEndpoint(client, parent_endpoint=self))
