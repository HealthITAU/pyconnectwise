from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesCountEndpoint import SalesOrdersStatusesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEndpoint import SalesOrdersStatusesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesInfoEndpoint import SalesOrdersStatusesInfoEndpoint
from pyconnectwise.models.manage import OrderStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOrdersStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOrdersStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesOrdersStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOrdersStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersStatusesIdEndpoint: The initialized SalesOrdersStatusesIdEndpoint object.
        """
        child = SalesOrdersStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderStatus]:
        """
        Performs a GET request against the /sales/orders/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OrderStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatus]:
        """
        Performs a GET request against the /sales/orders/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatus]: The parsed response data.
        """
        return self._parse_many(OrderStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatus]:
        """
        Performs a POST request against the /sales/orders/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatus]: The parsed response data.
        """
        return self._parse_many(OrderStatus, super()._make_request("POST", data=data, params=params).json())
