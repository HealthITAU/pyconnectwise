from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementManufacturersIdEndpoint import ProcurementManufacturersIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersCountEndpoint import ProcurementManufacturersCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersInfoEndpoint import ProcurementManufacturersInfoEndpoint
from pyconnectwise.models.manage.ManufacturerModel import ManufacturerModel

class ProcurementManufacturersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "manufacturers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementManufacturersCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementManufacturersInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementManufacturersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementManufacturersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementManufacturersIdEndpoint: The initialized ProcurementManufacturersIdEndpoint object.
        """
        child = ProcurementManufacturersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManufacturerModel]:
        """
        Performs a GET request against the /procurement/manufacturers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManufacturerModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManufacturerModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManufacturerModel]:
        """
        Performs a GET request against the /procurement/manufacturers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManufacturerModel]: The parsed response data.
        """
        return self._parse_many(ManufacturerModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManufacturerModel:
        """
        Performs a POST request against the /procurement/manufacturers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManufacturerModel: The parsed response data.
        """
        return self._parse_one(ManufacturerModel, super().make_request("POST", params=params).json())
        