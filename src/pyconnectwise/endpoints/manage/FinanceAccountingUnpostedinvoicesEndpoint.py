from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesCountEndpoint import \
    FinanceAccountingUnpostedinvoicesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedinvoicesIdEndpoint import \
    FinanceAccountingUnpostedinvoicesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import UnpostedInvoice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAccountingUnpostedinvoicesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnpostedInvoice], ConnectWiseManageRequestParams],
    IPaginateable[UnpostedInvoice, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "unpostedinvoices", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[UnpostedInvoice])
        IPaginateable.__init__(self, UnpostedInvoice)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedinvoicesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingUnpostedinvoicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedinvoicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedinvoicesIdEndpoint: The initialized FinanceAccountingUnpostedinvoicesIdEndpoint object.
        """
        child = FinanceAccountingUnpostedinvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[UnpostedInvoice]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[UnpostedInvoice]:
        """
        Performs a GET request against the /finance/accounting/unpostedinvoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedInvoice]: The parsed response data.
        """
        return self._parse_many(UnpostedInvoice, super()._make_request("GET", data=data, params=params).json())
