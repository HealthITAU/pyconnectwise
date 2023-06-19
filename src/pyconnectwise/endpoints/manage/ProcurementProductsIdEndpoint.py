from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementProductsIdDetachEndpoint import ProcurementProductsIdDetachEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdComponentsEndpoint import ProcurementProductsIdComponentsEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingShippingDetailsEndpoint import ProcurementProductsIdPickingShippingDetailsEndpoint
from pyconnectwise.models.manage.ProductItemModel import ProductItemModel

class ProcurementProductsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.detach = self.register_child_endpoint(
            ProcurementProductsIdDetachEndpoint(client, parent_endpoint=self)
        )
        self.components = self.register_child_endpoint(
            ProcurementProductsIdComponentsEndpoint(client, parent_endpoint=self)
        )
        self.pickingShippingDetails = self.register_child_endpoint(
            ProcurementProductsIdPickingShippingDetailsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductItemModel]:
        """
        Performs a GET request against the /procurement/products/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductItemModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProductItemModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductItemModel:
        """
        Performs a GET request against the /procurement/products/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductItemModel: The parsed response data.
        """
        return self._parse_one(ProductItemModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /procurement/products/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductItemModel:
        """
        Performs a PUT request against the /procurement/products/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductItemModel: The parsed response data.
        """
        return self._parse_one(ProductItemModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductItemModel:
        """
        Performs a PATCH request against the /procurement/products/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductItemModel: The parsed response data.
        """
        return self._parse_one(ProductItemModel, super().make_request("PATCH", params=params).json())
        