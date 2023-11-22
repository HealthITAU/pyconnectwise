from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint import (
    CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyPortalconfigurationsInvoicesetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "invoiceSetup", parent_endpoint=parent_endpoint)

        self.payment_processors = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint(client, parent_endpoint=self)
        )
