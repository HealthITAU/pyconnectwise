from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechStatusScanNetworkPortOption
from pyconnectwise.responses.paginated_response import PaginatedResponse


class LookupsStatusscannetworkportoptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Statusscannetworkportoptions", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechStatusScanNetworkPortOption]:
        """
        Performs a GET request against the /Lookups/Statusscannetworkportoptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechStatusScanNetworkPortOption]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechStatusScanNetworkPortOption,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[LabTechStatusScanNetworkPortOption]:
        """
        Performs a GET request against the /Lookups/Statusscannetworkportoptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechStatusScanNetworkPortOption]: The parsed response data.
        """
        return self._parse_many(
            LabTechStatusScanNetworkPortOption, super()._make_request("GET", data=data, params=params).json()
        )
