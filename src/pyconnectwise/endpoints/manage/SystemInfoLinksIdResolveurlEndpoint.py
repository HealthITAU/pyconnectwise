from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import LinkResolveUrlInfo
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemInfoLinksIdResolveurlEndpoint(
    ConnectWiseEndpoint, IPostable[LinkResolveUrlInfo, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "resolveurl", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, LinkResolveUrlInfo)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> LinkResolveUrlInfo:
        """
        Performs a POST request against the /system/info/links/{id}/resolveurl endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LinkResolveUrlInfo: The parsed response data.
        """
        return self._parse_one(
            LinkResolveUrlInfo,
            super()._make_request("POST", data=data, params=params).json(),
        )
