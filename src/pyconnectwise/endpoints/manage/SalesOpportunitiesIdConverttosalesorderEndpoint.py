from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import Order
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdConverttosalesorderEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "convertToSalesOrder", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Order:
        """
        Performs a POST request against the /sales/opportunities/{id}/convertToSalesOrder endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Order: The parsed response data.
        """
        return self._parse_one(Order, super()._make_request("POST", data=data, params=params).json())
