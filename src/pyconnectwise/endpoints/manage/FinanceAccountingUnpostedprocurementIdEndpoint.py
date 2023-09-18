from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdTaxablelevelsEndpoint import \
    FinanceAccountingUnpostedprocurementIdTaxablelevelsEndpoint
from pyconnectwise.models.manage import UnpostedProcurement
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingUnpostedprocurementIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.taxable_levels = self._register_child_endpoint(
            FinanceAccountingUnpostedprocurementIdTaxablelevelsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[UnpostedProcurement]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedProcurement]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), UnpostedProcurement, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UnpostedProcurement:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnpostedProcurement: The parsed response data.
        """
        return self._parse_one(UnpostedProcurement, super()._make_request("GET", data=data, params=params).json())
