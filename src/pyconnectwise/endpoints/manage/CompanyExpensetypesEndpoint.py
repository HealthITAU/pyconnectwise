from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyExpensetypesInfoEndpoint import CompanyExpensetypesInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyExpensetypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "expenseTypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyExpensetypesInfoEndpoint(client, parent_endpoint=self))
