from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import MarketplaceImport
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMarketplaceimportImportEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "import", parent_endpoint=parent_endpoint)

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MarketplaceImport:
        """
        Performs a POST request against the /system/marketplaceimport/import endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketplaceImport: The parsed response data.
        """
        return self._parse_one(MarketplaceImport, super()._make_request("POST", data=data, params=params).json())
