from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint import (
    CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint,
)


class CompanyPortalconfigurationsInvoicesetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "invoiceSetup", parent_endpoint=parent_endpoint
        )

        self.payment_processors = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint(
                client, parent_endpoint=self
            )
        )
