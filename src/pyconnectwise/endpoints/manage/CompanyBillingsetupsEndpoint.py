from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyBillingsetupsInfoEndpoint import CompanyBillingsetupsInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyBillingsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "billingSetups", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyBillingsetupsInfoEndpoint(client, parent_endpoint=self))
