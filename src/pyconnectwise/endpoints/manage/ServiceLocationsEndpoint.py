from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceLocationsIdEndpoint import ServiceLocationsIdEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsCountEndpoint import ServiceLocationsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceLocationsInfoEndpoint import ServiceLocationsInfoEndpoint
from pyconnectwise.models.manage.ServiceLocationModel import ServiceLocationModel

class ServiceLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceLocationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceLocationsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceLocationsIdEndpoint: The initialized ServiceLocationsIdEndpoint object.
        """
        child = ServiceLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ServiceLocationModel]:
        """
        Performs a GET request against the /service/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceLocationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ServiceLocationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ServiceLocationModel]:
        """
        Performs a GET request against the /service/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceLocationModel]: The parsed response data.
        """
        return self._parse_many(ServiceLocationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ServiceLocationModel:
        """
        Performs a POST request against the /service/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceLocationModel: The parsed response data.
        """
        return self._parse_one(ServiceLocationModel, super().make_request("POST", params=params).json())
        