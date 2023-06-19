from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsIdEndpoint import SystemDepartmentsIdLocationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsCountEndpoint import SystemDepartmentsIdLocationsCountEndpoint
from pyconnectwise.models.manage.DepartmentLocationModel import DepartmentLocationModel

class SystemDepartmentsIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemDepartmentsIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemDepartmentsIdLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDepartmentsIdLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDepartmentsIdLocationsIdEndpoint: The initialized SystemDepartmentsIdLocationsIdEndpoint object.
        """
        child = SystemDepartmentsIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DepartmentLocationModel]:
        """
        Performs a GET request against the /system/departments/{parentId}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentLocationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            DepartmentLocationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DepartmentLocationModel]:
        """
        Performs a GET request against the /system/departments/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentLocationModel]: The parsed response data.
        """
        return self._parse_many(DepartmentLocationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DepartmentLocationModel:
        """
        Performs a POST request against the /system/departments/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DepartmentLocationModel: The parsed response data.
        """
        return self._parse_one(DepartmentLocationModel, super().make_request("POST", params=params).json())
        