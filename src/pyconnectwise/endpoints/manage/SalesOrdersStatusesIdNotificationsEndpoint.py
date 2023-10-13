from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdNotificationsCountEndpoint import \
    SalesOrdersStatusesIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesIdNotificationsIdEndpoint import \
    SalesOrdersStatusesIdNotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import OrderStatusNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SalesOrdersStatusesIdNotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OrderStatusNotification], ConnectWiseManageRequestParams],
    IPostable[OrderStatusNotification, ConnectWiseManageRequestParams],
    IPaginateable[OrderStatusNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notifications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[OrderStatusNotification])
        IPostable.__init__(self, OrderStatusNotification)
        IPaginateable.__init__(self, OrderStatusNotification)

        self.count = self._register_child_endpoint(
            SalesOrdersStatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOrdersStatusesIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOrdersStatusesIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOrdersStatusesIdNotificationsIdEndpoint: The initialized SalesOrdersStatusesIdNotificationsIdEndpoint object.
        """
        child = SalesOrdersStatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[OrderStatusNotification]:
        """
        Performs a GET request against the /sales/orders/statuses/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatusNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), OrderStatusNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[OrderStatusNotification]:
        """
        Performs a GET request against the /sales/orders/statuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusNotification]: The parsed response data.
        """
        return self._parse_many(OrderStatusNotification, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> OrderStatusNotification:
        """
        Performs a POST request against the /sales/orders/statuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OrderStatusNotification: The parsed response data.
        """
        return self._parse_one(OrderStatusNotification, super()._make_request("POST", data=data, params=params).json())
