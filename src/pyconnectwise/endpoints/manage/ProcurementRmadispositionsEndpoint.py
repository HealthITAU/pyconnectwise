from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmadispositionsCountEndpoint import \
    ProcurementRmadispositionsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmadispositionsIdEndpoint import ProcurementRmadispositionsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmadispositionsInfoEndpoint import ProcurementRmadispositionsInfoEndpoint
from pyconnectwise.models.manage import RmaDisposition
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementRmadispositionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "RMADispositions", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementRmadispositionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementRmadispositionsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementRmadispositionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmadispositionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementRmadispositionsIdEndpoint: The initialized ProcurementRmadispositionsIdEndpoint object.
        """
        child = ProcurementRmadispositionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[RmaDisposition]:
        """
        Performs a GET request against the /procurement/RMADispositions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaDisposition]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), RmaDisposition, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaDisposition]:
        """
        Performs a GET request against the /procurement/RMADispositions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaDisposition]: The parsed response data.
        """
        return self._parse_many(RmaDisposition, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaDisposition:
        """
        Performs a POST request against the /procurement/RMADispositions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaDisposition: The parsed response data.
        """
        return self._parse_one(RmaDisposition, super()._make_request("POST", data=data, params=params).json())
