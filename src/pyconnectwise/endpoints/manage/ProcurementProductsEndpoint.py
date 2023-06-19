from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementProductsIdEndpoint import ProcurementProductsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsCountEndpoint import ProcurementProductsCountEndpoint
from pyconnectwise.models.manage.ProductItemModel import ProductItemModel

class ProcurementProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "products", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementProductsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdEndpoint: The initialized ProcurementProductsIdEndpoint object.
        """
        child = ProcurementProductsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductItemModel]:
        """
        Performs a GET request against the /procurement/products endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductItemModel]:
        """
        Performs a GET request against the /procurement/products endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductItemModel]: The parsed response data.
        """
        return self._parse_many(ProductItemModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductItemModel:
        """
        Performs a POST request against the /procurement/products endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductItemModel: The parsed response data.
        """
        return self._parse_one(ProductItemModel, super().make_request("POST", params=params).json())
        