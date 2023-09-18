from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdEmailtemplatesEndpoint import \
    ProcurementPurchaseorderstatusesIdEmailtemplatesEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdNotificationsEndpoint import \
    ProcurementPurchaseorderstatusesIdNotificationsEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdUsagesEndpoint import \
    ProcurementPurchaseorderstatusesIdUsagesEndpoint
from pyconnectwise.models.manage import PurchaseOrderStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseorderstatusesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.usages = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.emailtemplates = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdEmailtemplatesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PurchaseOrderStatus]:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PurchaseOrderStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderStatus:
        """
        Performs a GET request against the /procurement/purchaseorderstatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatus: The parsed response data.
        """
        return self._parse_one(PurchaseOrderStatus, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /procurement/purchaseorderstatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderStatus:
        """
        Performs a PATCH request against the /procurement/purchaseorderstatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatus: The parsed response data.
        """
        return self._parse_one(PurchaseOrderStatus, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderStatus:
        """
        Performs a PUT request against the /procurement/purchaseorderstatuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderStatus: The parsed response data.
        """
        return self._parse_one(PurchaseOrderStatus, super()._make_request("PUT", data=data, params=params).json())
