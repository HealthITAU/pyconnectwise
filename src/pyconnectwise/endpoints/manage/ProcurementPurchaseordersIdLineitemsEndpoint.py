from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdLineitemsBulkEndpoint import \
    ProcurementPurchaseordersIdLineitemsBulkEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdLineitemsCountEndpoint import \
    ProcurementPurchaseordersIdLineitemsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdLineitemsIdEndpoint import \
    ProcurementPurchaseordersIdLineitemsIdEndpoint
from pyconnectwise.models.manage import PurchaseOrderLineItem
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseordersIdLineitemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "lineitems", parent_endpoint=parent_endpoint)

        self.bulk = self._register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsBulkEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPurchaseordersIdLineitemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseordersIdLineitemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseordersIdLineitemsIdEndpoint: The initialized ProcurementPurchaseordersIdLineitemsIdEndpoint object.
        """
        child = ProcurementPurchaseordersIdLineitemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PurchaseOrderLineItem]:
        """
        Performs a GET request against the /procurement/purchaseorders/{id}/lineitems endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderLineItem]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PurchaseOrderLineItem, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PurchaseOrderLineItem]:
        """
        Performs a GET request against the /procurement/purchaseorders/{id}/lineitems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderLineItem]: The parsed response data.
        """
        return self._parse_many(PurchaseOrderLineItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderLineItem:
        """
        Performs a POST request against the /procurement/purchaseorders/{id}/lineitems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderLineItem: The parsed response data.
        """
        return self._parse_one(PurchaseOrderLineItem, super()._make_request("POST", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /procurement/purchaseorders/{id}/lineitems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
