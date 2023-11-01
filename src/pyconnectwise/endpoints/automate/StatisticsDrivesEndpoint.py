from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.automate import LabTechDriveStatistics
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class StatisticsDrivesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechDriveStatistics], ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Drives", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechDriveStatistics])

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechDriveStatistics]:
        """
        Performs a GET request against the /Statistics/Drives endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechDriveStatistics]: The parsed response data.
        """
        return self._parse_many(
            LabTechDriveStatistics,
            super()._make_request("GET", data=data, params=params).json(),
        )
