from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdRoutingsCountEndpoint import \
    FinanceBillingsetupsIdRoutingsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBillingsetupsIdRoutingsIdEndpoint import \
    FinanceBillingsetupsIdRoutingsIdEndpoint
from pyconnectwise.models.manage import BillingSetupRouting
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceBillingsetupsIdRoutingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "routings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            FinanceBillingsetupsIdRoutingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceBillingsetupsIdRoutingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBillingsetupsIdRoutingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBillingsetupsIdRoutingsIdEndpoint: The initialized FinanceBillingsetupsIdRoutingsIdEndpoint object.
        """
        child = FinanceBillingsetupsIdRoutingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[BillingSetupRouting]:
        """
        Performs a GET request against the /finance/billingSetups/{id}/routings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BillingSetupRouting]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), BillingSetupRouting, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BillingSetupRouting]:
        """
        Performs a GET request against the /finance/billingSetups/{id}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BillingSetupRouting]: The parsed response data.
        """
        return self._parse_many(BillingSetupRouting, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BillingSetupRouting:
        """
        Performs a POST request against the /finance/billingSetups/{id}/routings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BillingSetupRouting: The parsed response data.
        """
        return self._parse_one(BillingSetupRouting, super()._make_request("POST", data=data, params=params).json())
