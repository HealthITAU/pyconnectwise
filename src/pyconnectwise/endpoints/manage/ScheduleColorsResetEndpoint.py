from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import ScheduleColor
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleColorsResetEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reset", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ScheduleColor]:
        """
        Performs a POST request against the /schedule/colors/reset endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleColor]: The parsed response data.
        """
        return self._parse_many(ScheduleColor, super()._make_request("POST", data=data, params=params).json())
