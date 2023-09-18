from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingtermsCountEndpoint import FinanceBillingtermsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingtermsIdEndpoint import FinanceBillingtermsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingtermsInfoEndpoint import FinanceBillingtermsInfoEndpoint
from pyconnectwise.models.manage import BillingTerm
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceBillingtermsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingTerms", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceBillingtermsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceBillingtermsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceBillingtermsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingtermsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingtermsIdEndpoint: The initialized FinanceBillingtermsIdEndpoint object.
        """
        child = FinanceBillingtermsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BillingTerm]:
        """
        Performs a GET request against the /finance/billingTerms endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingTerm]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BillingTerm, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingTerm]:
        """
        Performs a GET request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingTerm]: The parsed response data.
        """
        return self._parse_many(BillingTerm, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingTerm:
        """
        Performs a POST request against the /finance/billingTerms endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingTerm: The parsed response data.
        """
        return self._parse_one(BillingTerm, super()._make_request("POST", data=data, params=params).json())
