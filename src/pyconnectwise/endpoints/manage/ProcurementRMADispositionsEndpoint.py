from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementRMADispositionsIdEndpoint import ProcurementRMADispositionsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRMADispositionsCountEndpoint import ProcurementRMADispositionsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRMADispositionsInfoEndpoint import ProcurementRMADispositionsInfoEndpoint
from pyconnectwise.models.manage.RmaDispositionModel import RmaDispositionModel

class ProcurementRMADispositionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "RMADispositions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRMADispositionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRMADispositionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementRMADispositionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRMADispositionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRMADispositionsIdEndpoint: The initialized ProcurementRMADispositionsIdEndpoint object.
        """
        child = ProcurementRMADispositionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaDispositionModel]:
        """
        Performs a GET request against the /procurement/RMADispositions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaDispositionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaDispositionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaDispositionModel]:
        """
        Performs a GET request against the /procurement/RMADispositions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaDispositionModel]: The parsed response data.
        """
        return self._parse_many(RmaDispositionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaDispositionModel:
        """
        Performs a POST request against the /procurement/RMADispositions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaDispositionModel: The parsed response data.
        """
        return self._parse_one(RmaDispositionModel, super().make_request("POST", params=params).json())
        