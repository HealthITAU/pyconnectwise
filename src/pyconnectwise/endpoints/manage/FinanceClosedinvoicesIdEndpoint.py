from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ClosedInvoice
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceClosedinvoicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ClosedInvoice:
        """
        Performs a PUT request against the /finance/closedInvoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ClosedInvoice: The parsed response data.
        """
        return self._parse_one(ClosedInvoice, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ClosedInvoice:
        """
        Performs a PATCH request against the /finance/closedInvoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ClosedInvoice: The parsed response data.
        """
        return self._parse_one(ClosedInvoice, super()._make_request("PATCH", data=data, params=params).json())
