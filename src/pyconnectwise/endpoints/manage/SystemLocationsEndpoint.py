from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemLocationsIdEndpoint import SystemLocationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsCountEndpoint import SystemLocationsCountEndpoint
from pyconnectwise.models.manage.LocationModel import LocationModel

class SystemLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLocationsIdEndpoint: The initialized SystemLocationsIdEndpoint object.
        """
        child = SystemLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LocationModel]:
        """
        Performs a GET request against the /system/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LocationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LocationModel]:
        """
        Performs a GET request against the /system/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationModel]: The parsed response data.
        """
        return self._parse_many(LocationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LocationModel:
        """
        Performs a POST request against the /system/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LocationModel: The parsed response data.
        """
        return self._parse_one(LocationModel, super().make_request("POST", params=params).json())
        