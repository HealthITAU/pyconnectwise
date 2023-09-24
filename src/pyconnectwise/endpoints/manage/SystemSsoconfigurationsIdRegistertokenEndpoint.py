from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import SsoConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemSsoconfigurationsIdRegistertokenEndpoint(
    ConnectWiseEndpoint, IPostable[SsoConfiguration, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "registertoken", parent_endpoint=parent_endpoint)

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
