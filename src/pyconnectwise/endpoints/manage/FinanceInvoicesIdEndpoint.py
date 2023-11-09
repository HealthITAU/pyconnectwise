from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPaymentsEndpoint import FinanceInvoicesIdPaymentsEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPdfEndpoint import FinanceInvoicesIdPdfEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import Invoice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceInvoicesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Invoice, ConnectWiseManageRequestParams],
    IPatchable[Invoice, ConnectWiseManageRequestParams],
    IPuttable[Invoice, ConnectWiseManageRequestParams],
    IPaginateable[Invoice, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Invoice)
        IPatchable.__init__(self, Invoice)
        IPuttable.__init__(self, Invoice)
        IPaginateable.__init__(self, Invoice)

        self.payments = self._register_child_endpoint(FinanceInvoicesIdPaymentsEndpoint(client, parent_endpoint=self))
        self.pdf = self._register_child_endpoint(FinanceInvoicesIdPdfEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Invoice]:
        """
        Performs a GET request against the /finance/invoices/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Invoice]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Invoice, self, page, page_size, params)

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Invoice:
        """
        Performs a GET request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Invoice: The parsed response data.
        """
        return self._parse_one(Invoice, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Invoice:
        """
        Performs a PATCH request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Invoice: The parsed response data.
        """
        return self._parse_one(Invoice, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Invoice:
        """
        Performs a PUT request against the /finance/invoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Invoice: The parsed response data.
        """
        return self._parse_one(Invoice, super()._make_request("PUT", data=data, params=params).json())
