from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesInfoEndpoint import CompanyExpensetypesInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyExpensetypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expenseTypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyExpensetypesInfoEndpoint(client, parent_endpoint=self))
