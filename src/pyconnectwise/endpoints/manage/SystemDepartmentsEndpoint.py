from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsCountEndpoint import SystemDepartmentsCountEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdEndpoint import SystemDepartmentsIdEndpoint
from pyconnectwise.models.manage import Department
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemDepartmentsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemDepartmentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemDepartmentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemDepartmentsIdEndpoint: The initialized SystemDepartmentsIdEndpoint object.
        """
        child = SystemDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Department]:
        """
        Performs a GET request against the /system/departments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Department]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Department, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Department]:
        """
        Performs a GET request against the /system/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Department]: The parsed response data.
        """
        return self._parse_many(Department, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Department:
        """
        Performs a POST request against the /system/departments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Department: The parsed response data.
        """
        return self._parse_one(Department, super()._make_request("POST", data=data, params=params).json())
