from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseClassificationsEndpoint import ExpenseClassificationsEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesEndpoint import ExpenseEntriesEndpoint
from pyconnectwise.endpoints.manage.ExpenseInfoEndpoint import ExpenseInfoEndpoint
from pyconnectwise.endpoints.manage.ExpensePaymenttypesEndpoint import ExpensePaymenttypesEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsEndpoint import ExpenseReportsEndpoint
from pyconnectwise.endpoints.manage.ExpenseTypesEndpoint import ExpenseTypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExpenseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expense", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ExpenseInfoEndpoint(client, parent_endpoint=self))
        self.payment_types = self._register_child_endpoint(ExpensePaymenttypesEndpoint(client, parent_endpoint=self))
        self.entries = self._register_child_endpoint(ExpenseEntriesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(ExpenseTypesEndpoint(client, parent_endpoint=self))
        self.classifications = self._register_child_endpoint(
            ExpenseClassificationsEndpoint(client, parent_endpoint=self)
        )
        self.reports = self._register_child_endpoint(ExpenseReportsEndpoint(client, parent_endpoint=self))
