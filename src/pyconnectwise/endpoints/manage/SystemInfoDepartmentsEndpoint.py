from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsCountEndpoint import SystemInfoDepartmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentsIdEndpoint import SystemInfoDepartmentsIdEndpoint
from pyconnectwise.models.manage import DepartmentInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemInfoDepartmentsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoDepartmentsIdEndpoint: The initialized SystemInfoDepartmentsIdEndpoint object.
        """
        child = SystemInfoDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[DepartmentInfo]:
        """
        Performs a GET request against the /system/info/departments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DepartmentInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DepartmentInfo]:
        """
        Performs a GET request against the /system/info/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentInfo]: The parsed response data.
        """
        return self._parse_many(DepartmentInfo, super()._make_request("GET", data=data, params=params).json())
