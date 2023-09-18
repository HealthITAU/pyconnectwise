from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmadispositionsInfoCountEndpoint import \
    ProcurementRmadispositionsInfoCountEndpoint
from pyconnectwise.models.manage import RmaDispositionInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmadispositionsInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementRmadispositionsInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[RmaDispositionInfo]:
        """
        Performs a GET request against the /procurement/RMADispositions/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaDispositionInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), RmaDispositionInfo, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaDispositionInfo]:
        """
        Performs a GET request against the /procurement/RMADispositions/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaDispositionInfo]: The parsed response data.
        """
        return self._parse_many(RmaDispositionInfo, super()._make_request("GET", data=data, params=params).json())
