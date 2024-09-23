from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.change_request import StatsMsg, StatsObject
from pyconnectwise.types import JSON, ConnectWiseChangeApprovalRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class GetStatsEndpoint(
    ConnectWiseEndpoint,
    IPostable[list[StatsMsg], ConnectWiseChangeApprovalRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        # TODO - Figure out a cleaner implementation for the endpoint URL
        ConnectWiseEndpoint.__init__(self, client, "change_request/dummy/getStats", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, list[StatsMsg])

    def post(
        self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None
    ) -> list[StatsMsg]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        obj = self._parse_one(StatsObject, super()._make_request("POST", data=data, params=params).json())
        return obj.msg
