from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdEmailtemplatesEndpoint import \
    SalesOrdersStatusesIdEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdInfoEndpoint import SalesOrdersStatusesIdInfoEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdNotificationsEndpoint import \
    SalesOrdersStatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdUsagesEndpoint import SalesOrdersStatusesIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import OrderStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesOrdersStatusesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[OrderStatus, ConnectWiseManageRequestParams],
    IPuttable[OrderStatus, ConnectWiseManageRequestParams],
    IPatchable[OrderStatus, ConnectWiseManageRequestParams],
    IPaginateable[OrderStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OrderStatus)
        IPuttable.__init__(self, OrderStatus)
        IPatchable.__init__(self, OrderStatus)
        IPaginateable.__init__(self, OrderStatus)

        self.usages = self._register_child_endpoint(SalesOrdersStatusesIdUsagesEndpoint(client, parent_endpoint=self))
        self.emailtemplates = self._register_child_endpoint(
            SalesOrdersStatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self._register_child_endpoint(
            SalesOrdersStatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(SalesOrdersStatusesIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[OrderStatus]:
        """
        Performs a GET request against the /sales/orders/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), OrderStatus, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> OrderStatus:
        """
        Performs a GET request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> OrderStatus:
        """
        Performs a PUT request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> OrderStatus:
        """
        Performs a PATCH request against the /sales/orders/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatus: The parsed response data.
        """
        return self._parse_one(OrderStatus, super()._make_request("PATCH", data=data, params=params).json())
