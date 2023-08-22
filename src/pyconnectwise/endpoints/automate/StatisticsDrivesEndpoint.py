from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechDriveStatistics
from pyconnectwise.responses.paginated_response import PaginatedResponse


class StatisticsDrivesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Drives", parent_endpoint=parent_endpoint)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechDriveStatistics]:
        """
        Performs a GET request against the /Statistics/Drives endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDriveStatistics]: The parsed response data.
        """
        return self._parse_many(LabTechDriveStatistics, super()._make_request("GET", data=data, params=params).json())
