from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingstatusesCountEndpoint import FinanceBillingstatusesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingstatusesIdEndpoint import FinanceBillingstatusesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingstatusesInfoEndpoint import FinanceBillingstatusesInfoEndpoint
from pyconnectwise.models.manage import BillingStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceBillingstatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "billingStatuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceBillingstatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceBillingstatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceBillingstatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingstatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingstatusesIdEndpoint: The initialized FinanceBillingstatusesIdEndpoint object.
        """
        child = FinanceBillingstatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BillingStatus]:
        """
        Performs a GET request against the /finance/billingStatuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BillingStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingStatus]:
        """
        Performs a GET request against the /finance/billingStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingStatus]: The parsed response data.
        """
        return self._parse_many(BillingStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingStatus:
        """
        Performs a POST request against the /finance/billingStatuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingStatus: The parsed response data.
        """
        return self._parse_one(BillingStatus, super()._make_request("POST", data=data, params=params).json())
