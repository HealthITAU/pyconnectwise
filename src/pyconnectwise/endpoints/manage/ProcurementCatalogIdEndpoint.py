from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInfoEndpoint import ProcurementCatalogIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdPricingEndpoint import ProcurementCatalogIdPricingEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsEndpoint import ProcurementCatalogIdComponentsEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInventoryEndpoint import ProcurementCatalogIdInventoryEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdMinimumStockByWarehouseEndpoint import ProcurementCatalogIdMinimumStockByWarehouseEndpoint
from pyconnectwise.models.manage.CatalogItemModel import CatalogItemModel

class ProcurementCatalogIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            ProcurementCatalogIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.pricing = self.register_child_endpoint(
            ProcurementCatalogIdPricingEndpoint(client, parent_endpoint=self)
        )
        self.components = self.register_child_endpoint(
            ProcurementCatalogIdComponentsEndpoint(client, parent_endpoint=self)
        )
        self.inventory = self.register_child_endpoint(
            ProcurementCatalogIdInventoryEndpoint(client, parent_endpoint=self)
        )
        self.minimumStockByWarehouse = self.register_child_endpoint(
            ProcurementCatalogIdMinimumStockByWarehouseEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CatalogItemModel]:
        """
        Performs a GET request against the /procurement/catalog/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogItemModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CatalogItemModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogItemModel:
        """
        Performs a GET request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItemModel: The parsed response data.
        """
        return self._parse_one(CatalogItemModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogItemModel:
        """
        Performs a PUT request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItemModel: The parsed response data.
        """
        return self._parse_one(CatalogItemModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogItemModel:
        """
        Performs a PATCH request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItemModel: The parsed response data.
        """
        return self._parse_one(CatalogItemModel, super().make_request("PATCH", params=params).json())
        