from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsCountEndpoint import \
    SystemInfoDepartmentlocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoDepartmentlocationsIdEndpoint import \
    SystemInfoDepartmentlocationsIdEndpoint
from pyconnectwise.models.manage import DepartmentLocationInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoDepartmentlocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departmentlocations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
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

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[DepartmentLocationInfo]:
        """
        Performs a GET request against the /system/info/departmentlocations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentLocationInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DepartmentLocationInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DepartmentLocationInfo]:
        """
        Performs a GET request against the /system/info/departmentlocations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentLocationInfo]: The parsed response data.
        """
        return self._parse_many(DepartmentLocationInfo, super()._make_request("GET", data=data, params=params).json())
