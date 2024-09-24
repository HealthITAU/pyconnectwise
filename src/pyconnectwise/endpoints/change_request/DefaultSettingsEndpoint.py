from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.change_request.SetSettingsEndpoint import SetSettingsEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class DefaultSettingsEndpoint(
    ConnectWiseEndpoint,
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "DefaultSettings", parent_endpoint=parent_endpoint)

    @property
    def set_settings(self) -> SetSettingsEndpoint:
        return SetSettingsEndpoint(self.client, parent_endpoint=self)
