from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersCountEndpoint import SalesOrdersCountEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersIdEndpoint import SalesOrdersIdEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesEndpoint import SalesOrdersStatusesEndpoint
from pyconnectwise.models.manage import Order
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOrdersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "orders", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOrdersCountEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(SalesOrdersStatusesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOrdersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersIdEndpoint: The initialized SalesOrdersIdEndpoint object.
        """
        child = SalesOrdersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Order]:
        """
        Performs a GET request against the /sales/orders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Order]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Order, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Order]:
        """
        Performs a GET request against the /sales/orders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Order]: The parsed response data.
        """
        return self._parse_many(Order, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Order:
        """
        Performs a POST request against the /sales/orders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Order: The parsed response data.
        """
        return self._parse_one(Order, super()._make_request("POST", data=data, params=params).json())
