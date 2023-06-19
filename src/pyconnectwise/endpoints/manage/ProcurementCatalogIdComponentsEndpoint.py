from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsIdEndpoint import ProcurementCatalogIdComponentsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsCountEndpoint import ProcurementCatalogIdComponentsCountEndpoint
from pyconnectwise.models.manage.CatalogComponentModel import CatalogComponentModel

class ProcurementCatalogIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogIdComponentsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementCatalogIdComponentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdComponentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdComponentsIdEndpoint: The initialized ProcurementCatalogIdComponentsIdEndpoint object.
        """
        child = ProcurementCatalogIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CatalogComponentModel]:
        """
        Performs a GET request against the /procurement/catalog/{parentId}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogComponentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CatalogComponentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CatalogComponentModel]:
        """
        Performs a GET request against the /procurement/catalog/{parentId}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogComponentModel]: The parsed response data.
        """
        return self._parse_many(CatalogComponentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogComponentModel:
        """
        Performs a POST request against the /procurement/catalog/{parentId}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogComponentModel: The parsed response data.
        """
        return self._parse_one(CatalogComponentModel, super().make_request("POST", params=params).json())
        