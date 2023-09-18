from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdLineitemsEndpoint import \
    ProcurementPurchaseordersIdLineitemsEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdRebatchEndpoint import \
    ProcurementPurchaseordersIdRebatchEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdUnbatchEndpoint import \
    ProcurementPurchaseordersIdUnbatchEndpoint
from pyconnectwise.models.manage import PurchaseOrder
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseordersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.lineitems = self._register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsEndpoint(client, parent_endpoint=self)
        )
        self.unbatch = self._register_child_endpoint(
            ProcurementPurchaseordersIdUnbatchEndpoint(client, parent_endpoint=self)
        )
        self.rebatch = self._register_child_endpoint(
            ProcurementPurchaseordersIdRebatchEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PurchaseOrder]:
        """
        Performs a GET request against the /procurement/purchaseorders/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrder]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PurchaseOrder, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrder:
        """
        Performs a GET request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(PurchaseOrder, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrder:
        """
        Performs a PUT request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(PurchaseOrder, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrder:
        """
        Performs a PATCH request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(PurchaseOrder, super()._make_request("PATCH", data=data, params=params).json())
