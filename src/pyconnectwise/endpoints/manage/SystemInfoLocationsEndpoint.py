from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsCountEndpoint import SystemInfoLocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInfoLocationsIdEndpoint import SystemInfoLocationsIdEndpoint
from pyconnectwise.models.manage import LocationInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemInfoLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemInfoLocationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemInfoLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInfoLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemInfoLocationsIdEndpoint: The initialized SystemInfoLocationsIdEndpoint object.
        """
        child = SystemInfoLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LocationInfo]:
        """
        Performs a GET request against the /system/info/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LocationInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LocationInfo]:
        """
        Performs a GET request against the /system/info/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LocationInfo]: The parsed response data.
        """
        return self._parse_many(LocationInfo, super()._make_request("GET", data=data, params=params).json())
