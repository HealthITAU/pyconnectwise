from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesIdTaxablelevelsEndpoint import \
    FinanceAccountingUnpostedinvoicesIdTaxablelevelsEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import UnpostedInvoice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAccountingUnpostedinvoicesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[UnpostedInvoice, ConnectWiseManageRequestParams],
    IPaginateable[UnpostedInvoice, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, UnpostedInvoice)
        IPaginateable.__init__(self, UnpostedInvoice)

        self.taxable_levels = self._register_child_endpoint(
            FinanceAccountingUnpostedinvoicesIdTaxablelevelsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[UnpostedInvoice]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedInvoice]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), UnpostedInvoice, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> UnpostedInvoice:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnpostedInvoice: The parsed response data.
        """
        return self._parse_one(UnpostedInvoice, super()._make_request("GET", data=data, params=params).json())
