from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementTypesIdEndpoint import ProcurementTypesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesCountEndpoint import ProcurementTypesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesInfoEndpoint import ProcurementTypesInfoEndpoint
from pyconnectwise.models.manage.ProductTypeModel import ProductTypeModel

class ProcurementTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementTypesIdEndpoint: The initialized ProcurementTypesIdEndpoint object.
        """
        child = ProcurementTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductTypeModel]:
        """
        Performs a GET request against the /procurement/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProductTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductTypeModel]:
        """
        Performs a GET request against the /procurement/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductTypeModel]: The parsed response data.
        """
        return self._parse_many(ProductTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductTypeModel:
        """
        Performs a POST request against the /procurement/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductTypeModel: The parsed response data.
        """
        return self._parse_one(ProductTypeModel, super().make_request("POST", params=params).json())
        