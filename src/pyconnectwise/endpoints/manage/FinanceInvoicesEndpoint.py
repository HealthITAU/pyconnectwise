from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesCountEndpoint import (
    FinanceInvoicesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceInvoicesIdEndpoint import (
    FinanceInvoicesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import Invoice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceInvoicesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Invoice], ConnectWiseManageRequestParams],
    IPostable[Invoice, ConnectWiseManageRequestParams],
    IPaginateable[Invoice, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "invoices", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Invoice])
        IPostable.__init__(self, Invoice)
        IPaginateable.__init__(self, Invoice)

        self.count = self._register_child_endpoint(
            FinanceInvoicesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceInvoicesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInvoicesIdEndpoint: The initialized FinanceInvoicesIdEndpoint object.
        """
        child = FinanceInvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Invoice]:
        """
        Performs a GET request against the /finance/invoices endpoint and returns an initialized PaginatedResponse object.

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
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Invoice,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Invoice]:
        """
        Performs a GET request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Invoice]: The parsed response data.
        """
        return self._parse_many(
            Invoice, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Invoice:
        """
        Performs a POST request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Invoice: The parsed response data.
        """
        return self._parse_one(
            Invoice, super()._make_request("POST", data=data, params=params).json()
        )
