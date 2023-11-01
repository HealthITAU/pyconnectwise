from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyBillingsetupsInfoEndpoint import (
    CompanyBillingsetupsInfoEndpoint,
)


class CompanyBillingsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "billingSetups", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            CompanyBillingsetupsInfoEndpoint(client, parent_endpoint=self)
        )
