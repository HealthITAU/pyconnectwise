from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdPaymentsIdEndpoint import FinanceInvoicesIdPaymentsIdEndpoint
from pyconnectwise.models.manage import InvoicePayment
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceInvoicesIdPaymentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "payments", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), InvoicePayment, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InvoicePayment]:
        """
        Performs a GET request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InvoicePayment]: The parsed response data.
        """
        return self._parse_many(InvoicePayment, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> InvoicePayment:
        """
        Performs a POST request against the /finance/invoices/{id}/payments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InvoicePayment: The parsed response data.
        """
        return self._parse_one(InvoicePayment, super()._make_request("POST", data=data, params=params).json())
