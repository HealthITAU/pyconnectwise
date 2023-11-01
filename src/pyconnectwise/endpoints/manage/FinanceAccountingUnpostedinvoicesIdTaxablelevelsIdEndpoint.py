from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import UnpostedInvoiceTaxableLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceAccountingUnpostedinvoicesIdTaxablelevelsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[UnpostedInvoiceTaxableLevel, ConnectWiseManageRequestParams],
    IPaginateable[UnpostedInvoiceTaxableLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, UnpostedInvoiceTaxableLevel)
        IPaginateable.__init__(self, UnpostedInvoiceTaxableLevel)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[UnpostedInvoiceTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id}/taxableLevels/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedInvoiceTaxableLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UnpostedInvoiceTaxableLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> UnpostedInvoiceTaxableLevel:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices/{id}/taxableLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnpostedInvoiceTaxableLevel: The parsed response data.
        """
        return self._parse_one(
            UnpostedInvoiceTaxableLevel,
            super()._make_request("GET", data=data, params=params).json(),
        )
