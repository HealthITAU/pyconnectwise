from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Repositories.MySQL.Domain.Models.NetworkProbe import (
    StatusScanNetworkPortOption,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class LookupsStatusscannetworkportoptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(
            client, "Statusscannetworkportoptions", parent_endpoint=parent_endpoint
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[StatusScanNetworkPortOption]:
        """
        Performs a GET request against the /Lookups/Statusscannetworkportoptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[StatusScanNetworkPortOption]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            StatusScanNetworkPortOption,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[StatusScanNetworkPortOption]:
        """
        Performs a GET request against the /Lookups/Statusscannetworkportoptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[StatusScanNetworkPortOption]: The parsed response data.
        """
        return self._parse_many(
            StatusScanNetworkPortOption,
            super()._make_request("GET", data=data, params=params).json(),
        )
