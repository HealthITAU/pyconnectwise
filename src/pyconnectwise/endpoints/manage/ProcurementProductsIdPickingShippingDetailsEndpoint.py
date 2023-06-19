from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingShippingDetailsIdEndpoint import ProcurementProductsIdPickingShippingDetailsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingShippingDetailsCountEndpoint import ProcurementProductsIdPickingShippingDetailsCountEndpoint
from pyconnectwise.models.manage.ProductPickingShippingDetailModel import ProductPickingShippingDetailModel

class ProcurementProductsIdPickingShippingDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "pickingShippingDetails", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsIdPickingShippingDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementProductsIdPickingShippingDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdPickingShippingDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdPickingShippingDetailsIdEndpoint: The initialized ProcurementProductsIdPickingShippingDetailsIdEndpoint object.
        """
        child = ProcurementProductsIdPickingShippingDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductPickingShippingDetailModel]:
        """
        Performs a GET request against the /procurement/products/{parentId}/pickingShippingDetails endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductPickingShippingDetailModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProductPickingShippingDetailModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductPickingShippingDetailModel]:
        """
        Performs a GET request against the /procurement/products/{parentId}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetailModel]: The parsed response data.
        """
        return self._parse_many(ProductPickingShippingDetailModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductPickingShippingDetailModel]:
        """
        Performs a POST request against the /procurement/products/{parentId}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetailModel]: The parsed response data.
        """
        return self._parse_many(ProductPickingShippingDetailModel, super().make_request("POST", params=params).json())
        