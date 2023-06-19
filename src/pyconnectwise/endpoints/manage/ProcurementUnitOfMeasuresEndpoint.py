from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementUnitOfMeasuresIdEndpoint import ProcurementUnitOfMeasuresIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitOfMeasuresCountEndpoint import ProcurementUnitOfMeasuresCountEndpoint
from pyconnectwise.models.manage.UnitOfMeasureModel import UnitOfMeasureModel

class ProcurementUnitOfMeasuresEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unitOfMeasures", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementUnitOfMeasuresCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementUnitOfMeasuresIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementUnitOfMeasuresIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementUnitOfMeasuresIdEndpoint: The initialized ProcurementUnitOfMeasuresIdEndpoint object.
        """
        child = ProcurementUnitOfMeasuresIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UnitOfMeasureModel]:
        """
        Performs a GET request against the /procurement/unitOfMeasures endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnitOfMeasureModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UnitOfMeasureModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UnitOfMeasureModel]:
        """
        Performs a GET request against the /procurement/unitOfMeasures endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnitOfMeasureModel]: The parsed response data.
        """
        return self._parse_many(UnitOfMeasureModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> UnitOfMeasureModel:
        """
        Performs a POST request against the /procurement/unitOfMeasures endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnitOfMeasureModel: The parsed response data.
        """
        return self._parse_one(UnitOfMeasureModel, super().make_request("POST", params=params).json())
        