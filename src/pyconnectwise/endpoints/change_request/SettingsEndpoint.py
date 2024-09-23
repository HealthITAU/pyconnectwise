from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.change_request.DefaultSettingsEndpoint import DefaultSettingsEndpoint
from pyconnectwise.interfaces import IGettable
from pyconnectwise.models.change_request import SettingsData, SettingsObject
from pyconnectwise.types import JSON, ConnectWiseChangeApprovalRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SettingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SettingsData], ConnectWiseChangeApprovalRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "settings", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SettingsData])

    def get(
        self, data: JSON | None = None, params: ConnectWiseChangeApprovalRequestParams | None = None
    ) -> list[SettingsData]:
        """
        Performs a GET request against the /api/change_requests endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChangeRequestMsg]: The parsed response data.
        """
        obj = self._parse_one(SettingsObject, super()._make_request("GET", data=data, params=params).json())
        # TODO - `total`, `current`, which is paginated?
        return obj.msg.data

    @property
    def default_settings(self) -> DefaultSettingsEndpoint:
        """
        Get the default settings for change requests.

        Returns:
            SettingsData: The parsed response data.
        """
        return DefaultSettingsEndpoint(self.client, parent_endpoint=self)

