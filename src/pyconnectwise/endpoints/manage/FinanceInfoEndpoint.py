from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoCurrencycodesEndpoint import FinanceInfoCurrencycodesEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoInvoiceEndpoint import FinanceInfoInvoiceEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoTaxintegrationsEndpoint import FinanceInfoTaxintegrationsEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)

        self.currency_codes = self._register_child_endpoint(
            FinanceInfoCurrencycodesEndpoint(client, parent_endpoint=self)
        )
        self.invoice = self._register_child_endpoint(FinanceInfoInvoiceEndpoint(client, parent_endpoint=self))
        self.tax_integrations = self._register_child_endpoint(
            FinanceInfoTaxintegrationsEndpoint(client, parent_endpoint=self)
        )
