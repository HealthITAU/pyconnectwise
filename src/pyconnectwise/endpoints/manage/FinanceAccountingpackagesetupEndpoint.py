from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesetupCountEndpoint import \
    FinanceAccountingpackagesetupCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingpackagesetupIdEndpoint import \
    FinanceAccountingpackagesetupIdEndpoint
from pyconnectwise.models.manage import AccountingPackageSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAccountingpackagesetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackageSetup", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceAccountingpackagesetupCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingpackagesetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingpackagesetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingpackagesetupIdEndpoint: The initialized FinanceAccountingpackagesetupIdEndpoint object.
        """
        child = FinanceAccountingpackagesetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AccountingPackageSetup]:
        """
        Performs a GET request against the /finance/accountingPackageSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingPackageSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AccountingPackageSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AccountingPackageSetup]:
        """
        Performs a GET request against the /finance/accountingPackageSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingPackageSetup]: The parsed response data.
        """
        return self._parse_many(AccountingPackageSetup, super()._make_request("GET", data=data, params=params).json())
