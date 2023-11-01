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
from pyconnectwise.models.manage import ScheduleColor
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ScheduleColorsIdClearEndpoint(
    ConnectWiseEndpoint, IPostable[ScheduleColor, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "clear", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, ScheduleColor)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ScheduleColor:
        """
        Performs a POST request against the /schedule/colors/{id}/clear endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleColor: The parsed response data.
        """
        return self._parse_one(
            ScheduleColor,
            super()._make_request("POST", data=data, params=params).json(),
        )
