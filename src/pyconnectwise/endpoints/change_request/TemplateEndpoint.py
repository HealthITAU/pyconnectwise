from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable
from pyconnectwise.models.change_request import TemplateData, TemplateObject
from pyconnectwise.types import JSON, ConnectWiseChangeApprovalRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class TemplateEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TemplateData], ConnectWiseChangeApprovalRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "template", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TemplateData])

    def get(
        self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None
    ) -> list[TemplateData]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        obj = self._parse_one(TemplateObject, super()._make_request("GET", data=data, params=params).json())
        return obj.msg.data
