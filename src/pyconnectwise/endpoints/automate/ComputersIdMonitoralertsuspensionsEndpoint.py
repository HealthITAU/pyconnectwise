from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechMonitorAlertSuspension
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdMonitoralertsuspensionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Monitoralertsuspensions", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechMonitorAlertSuspension:
        """
        Performs a POST request against the /Computers/{id}/Monitoralertsuspensions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechMonitorAlertSuspension: The parsed response data.
        """
        return self._parse_one(
            LabTechMonitorAlertSuspension, super()._make_request("POST", data=data, params=params).json()
        )
