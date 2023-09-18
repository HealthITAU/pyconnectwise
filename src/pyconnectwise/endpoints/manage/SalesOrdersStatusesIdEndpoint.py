from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesEndpoint import \
    SalesOrdersStatusesIdEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdInfoEndpoint import SalesOrdersStatusesIdInfoEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdNotificationsEndpoint import \
    SalesOrdersStatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdUsagesEndpoint import SalesOrdersStatusesIdUsagesEndpoint
from pyconnectwise.models.manage import OrderStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOrdersStatusesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SalesOrdersStatusesIdInfoEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(SalesOrdersStatusesIdUsagesEndpoint(client, parent_endpoint=self))
        self.notifications = self._register_child_endpoint(
            SalesOrdersStatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.emailtemplates = self._register_child_endpoint(
            SalesOrdersStatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderStatus]:
        """
        Performs a GET request against the /sales/orders/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OrderStatus:
        """
        Performs a GET request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OrderStatus:
        """
        Performs a PUT request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OrderStatus:
        """
        Performs a PATCH request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("PATCH", data=data, params=params).json())
