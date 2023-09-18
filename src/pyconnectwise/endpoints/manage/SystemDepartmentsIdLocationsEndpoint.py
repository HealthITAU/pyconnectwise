from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsCountEndpoint import \
    SystemDepartmentsIdLocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemDepartmentsIdLocationsIdEndpoint import SystemDepartmentsIdLocationsIdEndpoint
from pyconnectwise.models.manage import DepartmentLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemDepartmentsIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
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

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[DepartmentLocation]:
        """
        Performs a GET request against the /system/departments/{id}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DepartmentLocation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DepartmentLocation, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DepartmentLocation]:
        """
        Performs a GET request against the /system/departments/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DepartmentLocation]: The parsed response data.
        """
        return self._parse_many(DepartmentLocation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DepartmentLocation:
        """
        Performs a POST request against the /system/departments/{id}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DepartmentLocation: The parsed response data.
        """
        return self._parse_one(DepartmentLocation, super()._make_request("POST", data=data, params=params).json())
