from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementManufacturersCountInfoEndpoint import ProcurementManufacturersCountInfoEndpoint
from pyconnectwise.models.manage.CountModel import CountModel

class ProcurementManufacturersCountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "count", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            ProcurementManufacturersCountInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CountModel]:
        """
        Performs a GET request against the /procurement/manufacturers/count endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CountModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CountModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CountModel:
        """
        Performs a GET request against the /procurement/manufacturers/count endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CountModel: The parsed response data.
        """
        return self._parse_one(CountModel, super().make_request("GET", params=params).json())
        