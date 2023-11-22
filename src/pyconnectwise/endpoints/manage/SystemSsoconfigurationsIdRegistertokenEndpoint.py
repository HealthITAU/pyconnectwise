from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.manage import SsoConfiguration
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemSsoconfigurationsIdRegistertokenEndpoint(
    ConnectWiseEndpoint, IPostable[SsoConfiguration, ConnectWiseManageRequestParams]
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "registertoken", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, SsoConfiguration)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SsoConfiguration:
        """
        Performs a POST request against the /system/ssoConfigurations/{id}/registertoken endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SsoConfiguration: The parsed response data.
        """
        return self._parse_one(SsoConfiguration, super()._make_request("POST", data=data, params=params).json())
