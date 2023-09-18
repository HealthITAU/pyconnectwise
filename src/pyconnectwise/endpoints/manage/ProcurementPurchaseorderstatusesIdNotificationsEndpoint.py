from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint import \
    ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint import \
    ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint
from pyconnectwise.models.manage import PurchaseOrderStatusNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseorderstatusesIdNotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notifications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint: The initialized ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint object.
        """
        child = ProcurementPurchaseorderstatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PurchaseOrderStatusNotification]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderStatusNotification]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PurchaseOrderStatusNotification, self, page, page_size, params
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[PurchaseOrderStatusNotification]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderStatusNotification]: The parsed response data.
        """
        return self._parse_many(
            PurchaseOrderStatusNotification, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderStatusNotification:
        """
        Performs a POST request against the /procurement/purchaseorderstatuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatusNotification: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrderStatusNotification, super()._make_request("POST", data=data, params=params).json()
        )
