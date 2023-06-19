from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsIdEndpoint import SystemInfoDepartmentlocationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsCountEndpoint import SystemInfoDepartmentlocationsCountEndpoint
from pyconnectwise.models.manage.DepartmentLocationInfoModel import DepartmentLocationInfoModel

class SystemInfoDepartmentlocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departmentlocations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoDepartmentlocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemInfoDepartmentlocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoDepartmentlocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoDepartmentlocationsIdEndpoint: The initialized SystemInfoDepartmentlocationsIdEndpoint object.
        """
        child = SystemInfoDepartmentlocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DepartmentLocationInfoModel]:
        """
        Performs a GET request against the /system/info/departmentlocations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentLocationInfoModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            DepartmentLocationInfoModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DepartmentLocationInfoModel]:
        """
        Performs a GET request against the /system/info/departmentlocations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentLocationInfoModel]: The parsed response data.
        """
        return self._parse_many(DepartmentLocationInfoModel, super().make_request("GET", params=params).json())
        