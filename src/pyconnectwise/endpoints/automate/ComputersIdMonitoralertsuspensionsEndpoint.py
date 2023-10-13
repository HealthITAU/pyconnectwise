from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechMonitorAlertSuspension
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ComputersIdMonitoralertsuspensionsEndpoint(
    ConnectWiseEndpoint, IPostable[LabTechMonitorAlertSuspension, ConnectWiseAutomateRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Monitoralertsuspensions", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, LabTechMonitorAlertSuspension)

    def post(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechMonitorAlertSuspension:
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
