from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesCountEndpoint import FinanceInvoicesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceInvoicesIdEndpoint import FinanceInvoicesIdEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import Invoice
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceInvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoices", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceInvoicesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceInvoicesIdEndpoint:
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

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Invoice]:
        """
        Performs a GET request against the /finance/invoices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Invoice]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Invoice,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Invoice]:
        """
        Performs a GET request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Invoice]: The parsed response data.
        """
        return self._parse_many(Invoice, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Invoice:
        """
        Performs a POST request against the /finance/invoices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Invoice: The parsed response data.
        """
        return self._parse_one(Invoice, super()._make_request("POST", data=data, params=params).json())