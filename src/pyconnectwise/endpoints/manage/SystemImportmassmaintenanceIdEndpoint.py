from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.manage import ImportMassMaintenance
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemImportmassmaintenanceIdEndpoint(
    ConnectWiseEndpoint, IPostable[ImportMassMaintenance, ConnectWiseManageRequestParams]
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, ImportMassMaintenance)

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ImportMassMaintenance:
        """
        Performs a POST request against the /system/importMassMaintenance/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ImportMassMaintenance: The parsed response data.
        """
        return self._parse_one(ImportMassMaintenance, super()._make_request("POST", data=data, params=params).json())
