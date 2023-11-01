from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPaymentsIdEndpoint import (
    FinanceInvoicesIdPaymentsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import InvoicePayment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceInvoicesIdPaymentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InvoicePayment], ConnectWiseManageRequestParams],
    IPostable[InvoicePayment, ConnectWiseManageRequestParams],
    IPaginateable[InvoicePayment, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "payments", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[InvoicePayment])
        IPostable.__init__(self, InvoicePayment)
        IPaginateable.__init__(self, InvoicePayment)

    def id(self, id: int) -> FinanceInvoicesIdPaymentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoicesIdPaymentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoicesIdPaymentsIdEndpoint: The initialized FinanceInvoicesIdPaymentsIdEndpoint object.
        """
        child = FinanceInvoicesIdPaymentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[InvoicePayment]:
        """
        Performs a GET request against the /finance/invoices/{id}/payments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InvoicePayment]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            InvoicePayment,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[InvoicePayment]:
        """
        Performs a GET request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoicePayment]: The parsed response data.
        """
        return self._parse_many(
            InvoicePayment,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> InvoicePayment:
        """
        Performs a POST request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoicePayment: The parsed response data.
        """
        return self._parse_one(
            InvoicePayment,
            super()._make_request("POST", data=data, params=params).json(),
        )
