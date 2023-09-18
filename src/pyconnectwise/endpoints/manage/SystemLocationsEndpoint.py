from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsCountEndpoint import SystemLocationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemLocationsIdEndpoint import SystemLocationsIdEndpoint
from pyconnectwise.models.manage import Location
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemLocationsCountEndpoint(client, parent_endpoint=self))

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

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Location]:
        """
        Performs a GET request against the /system/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Location]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Location, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Location]:
        """
        Performs a GET request against the /system/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Location]: The parsed response data.
        """
        return self._parse_many(Location, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Location:
        """
        Performs a POST request against the /system/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Location: The parsed response data.
        """
        return self._parse_one(Location, super()._make_request("POST", data=data, params=params).json())
