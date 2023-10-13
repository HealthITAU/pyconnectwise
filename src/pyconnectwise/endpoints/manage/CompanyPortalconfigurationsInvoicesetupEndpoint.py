from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint import \
    CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyPortalconfigurationsInvoicesetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "invoiceSetup", parent_endpoint=parent_endpoint)

        self.payment_processors = self._register_child_endpoint(
            CompanyPortalconfigurationsInvoicesetupPaymentprocessorsEndpoint(client, parent_endpoint=self)
        )
