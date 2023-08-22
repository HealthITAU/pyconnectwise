from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyBillingsetupsInfoEndpoint import CompanyBillingsetupsInfoEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyBillingsetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingSetups", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyBillingsetupsInfoEndpoint(client, parent_endpoint=self))
