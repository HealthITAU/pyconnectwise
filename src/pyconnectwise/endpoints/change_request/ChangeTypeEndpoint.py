from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdEndpoint import ServiceTicketsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.change_request import ChangeRequestMsg, ChangeTypeData
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ChangeTypeEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ChangeRequestMsg], ConnectWiseManageRequestParams],
    IPostable[ChangeRequestMsg, ConnectWiseManageRequestParams],
    IPaginateable[ChangeRequestMsg, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "change_type", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ChangeTypeData])

        # TODO - Handle paginated?

        # TODO - Figure out if there are other endpoints!
        # TODO - Handle the fact that the TLD is different!

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[ChangeTypeData]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeTypeData]: The parsed response data.
        """
        # TODO - Throw out the msg total, current information
        return self._parse_many(ChangeTypeData, super()._make_request("GET", data=data, params=params).json())
