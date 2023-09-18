from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersCountEndpoint import ProcurementPurchaseordersCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdEndpoint import ProcurementPurchaseordersIdEndpoint
from pyconnectwise.models.manage import PurchaseOrder
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseordersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "purchaseorders", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementPurchaseordersCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementPurchaseordersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseordersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseordersIdEndpoint: The initialized ProcurementPurchaseordersIdEndpoint object.
        """
        child = ProcurementPurchaseordersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PurchaseOrder]:
        """
        Performs a GET request against the /procurement/purchaseorders endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PurchaseOrder]:
        """
        Performs a GET request against the /procurement/purchaseorders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrder]: The parsed response data.
        """
        return self._parse_many(PurchaseOrder, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrder:
        """
        Performs a POST request against the /procurement/purchaseorders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(PurchaseOrder, super()._make_request("POST", data=data, params=params).json())
