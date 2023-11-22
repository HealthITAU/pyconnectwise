from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPaymentsIdEndpoint import FinanceInvoicesIdPaymentsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Payment
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceInvoicesIdPaymentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Payment], ConnectWiseManageRequestParams],
    IPostable[Payment, ConnectWiseManageRequestParams],
    IPaginateable[Payment, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "payments", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Payment])
        IPostable.__init__(self, Payment)
        IPaginateable.__init__(self, Payment)

    def id(self, _id: int) -> FinanceInvoicesIdPaymentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInvoicesIdPaymentsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceInvoicesIdPaymentsIdEndpoint: The initialized FinanceInvoicesIdPaymentsIdEndpoint object.
        """
        child = FinanceInvoicesIdPaymentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Payment]:
        """
        Performs a GET request against the /finance/invoices/{id}/payments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Payment]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Payment, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Payment]:
        """
        Performs a GET request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Payment]: The parsed response data.
        """
        return self._parse_many(Payment, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Payment:
        """
        Performs a POST request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Payment: The parsed response data.
        """
        return self._parse_one(Payment, super()._make_request("POST", data=data, params=params).json())
