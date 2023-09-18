from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import UnpostedExpenseTaxableLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[UnpostedExpenseTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{id}/taxableLevels/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpenseTaxableLevel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), UnpostedExpenseTaxableLevel, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UnpostedExpenseTaxableLevel:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{id}/taxableLevels/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnpostedExpenseTaxableLevel: The parsed response data.
        """
        return self._parse_one(
            UnpostedExpenseTaxableLevel, super()._make_request("GET", data=data, params=params).json()
        )
