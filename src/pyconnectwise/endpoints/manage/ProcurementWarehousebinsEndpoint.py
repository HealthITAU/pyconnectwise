from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsCountEndpoint import ProcurementWarehousebinsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdEndpoint import ProcurementWarehousebinsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsInfoEndpoint import ProcurementWarehousebinsInfoEndpoint
from pyconnectwise.models.manage import WarehouseBin
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementWarehousebinsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "warehouseBins", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementWarehousebinsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementWarehousebinsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementWarehousebinsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementWarehousebinsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementWarehousebinsIdEndpoint: The initialized ProcurementWarehousebinsIdEndpoint object.
        """
        child = ProcurementWarehousebinsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[WarehouseBin]:
        """
        Performs a GET request against the /procurement/warehouseBins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WarehouseBin]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), WarehouseBin, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WarehouseBin]:
        """
        Performs a GET request against the /procurement/warehouseBins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WarehouseBin]: The parsed response data.
        """
        return self._parse_many(WarehouseBin, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WarehouseBin:
        """
        Performs a POST request against the /procurement/warehouseBins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBin: The parsed response data.
        """
        return self._parse_one(WarehouseBin, super()._make_request("POST", data=data, params=params).json())
