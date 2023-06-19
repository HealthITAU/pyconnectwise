from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementCategoriesIdEndpoint import ProcurementCategoriesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesCountEndpoint import ProcurementCategoriesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesInfoEndpoint import ProcurementCategoriesInfoEndpoint
from pyconnectwise.models.manage.CategoryModel import CategoryModel

class ProcurementCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "categories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCategoriesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementCategoriesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementCategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCategoriesIdEndpoint: The initialized ProcurementCategoriesIdEndpoint object.
        """
        child = ProcurementCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CategoryModel]:
        """
        Performs a GET request against the /procurement/categories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CategoryModel]:
        """
        Performs a GET request against the /procurement/categories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CategoryModel]: The parsed response data.
        """
        return self._parse_many(CategoryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CategoryModel:
        """
        Performs a POST request against the /procurement/categories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CategoryModel: The parsed response data.
        """
        return self._parse_one(CategoryModel, super().make_request("POST", params=params).json())
        