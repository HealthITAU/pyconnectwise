from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementCatalogIdEndpoint import ProcurementCatalogIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogCountEndpoint import ProcurementCatalogCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogInfoEndpoint import ProcurementCatalogInfoEndpoint
from pyconnectwise.models.manage.CatalogItemModel import CatalogItemModel

class ProcurementCatalogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "catalog", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementCatalogInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementCatalogIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdEndpoint: The initialized ProcurementCatalogIdEndpoint object.
        """
        child = ProcurementCatalogIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CatalogItemModel]:
        """
        Performs a GET request against the /procurement/catalog endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CatalogItemModel]:
        """
        Performs a GET request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogItemModel]: The parsed response data.
        """
        return self._parse_many(CatalogItemModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogItemModel:
        """
        Performs a POST request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItemModel: The parsed response data.
        """
        return self._parse_one(CatalogItemModel, super().make_request("POST", params=params).json())
        