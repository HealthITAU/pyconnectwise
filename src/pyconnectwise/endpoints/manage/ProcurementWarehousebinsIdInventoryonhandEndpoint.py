from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdInventoryonhandCountEndpoint import \
    ProcurementWarehousebinsIdInventoryonhandCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdInventoryonhandIdEndpoint import \
    ProcurementWarehousebinsIdInventoryonhandIdEndpoint
from pyconnectwise.models.manage import InventoryOnHand
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementWarehousebinsIdInventoryonhandEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inventoryOnHand", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementWarehousebinsIdInventoryonhandCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementWarehousebinsIdInventoryonhandIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementWarehousebinsIdInventoryonhandIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementWarehousebinsIdInventoryonhandIdEndpoint: The initialized ProcurementWarehousebinsIdInventoryonhandIdEndpoint object.
        """
        child = ProcurementWarehousebinsIdInventoryonhandIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[InventoryOnHand]:
        """
        Performs a GET request against the /procurement/warehouseBins/{id}/inventoryOnHand endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InventoryOnHand]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), InventoryOnHand, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InventoryOnHand]:
        """
        Performs a GET request against the /procurement/warehouseBins/{id}/inventoryOnHand endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InventoryOnHand]: The parsed response data.
        """
        return self._parse_many(InventoryOnHand, super()._make_request("GET", data=data, params=params).json())
