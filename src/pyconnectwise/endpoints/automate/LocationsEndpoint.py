from typing import Any

from pyconnectwise.endpoints.automate.LocationsIdEndpoint import LocationsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateLocation, LabTechLocation
from pyconnectwise.responses.paginated_response import PaginatedResponse


class LocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Locations", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> LocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized LocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            LocationsIdEndpoint: The initialized LocationsIdEndpoint object.
        """
        child = LocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AutomateLocation]:
        """
        Performs a GET request against the /Locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateLocation]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AutomateLocation, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AutomateLocation]:
        """
        Performs a GET request against the /Locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateLocation]: The parsed response data.
        """
        return self._parse_many(AutomateLocation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechLocation:
        """
        Performs a POST request against the /Locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechLocation: The parsed response data.
        """
        return self._parse_one(LabTechLocation, super()._make_request("POST", data=data, params=params).json())
