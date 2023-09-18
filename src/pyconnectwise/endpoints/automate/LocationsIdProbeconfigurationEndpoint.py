from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechProbeConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class LocationsIdProbeconfigurationEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Probeconfiguration", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechProbeConfiguration]:
        """
        Performs a GET request against the /Locations/{id}/Probeconfiguration endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProbeConfiguration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechProbeConfiguration, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechProbeConfiguration:
        """
        Performs a GET request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(LabTechProbeConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechProbeConfiguration:
        """
        Performs a POST request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration, super()._make_request("POST", data=data, params=params).json()
        )

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechProbeConfiguration:
        """
        Performs a PATCH request against the /Locations/{id}/Probeconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProbeConfiguration: The parsed response data.
        """
        return self._parse_one(
            LabTechProbeConfiguration, super()._make_request("PATCH", data=data, params=params).json()
        )
