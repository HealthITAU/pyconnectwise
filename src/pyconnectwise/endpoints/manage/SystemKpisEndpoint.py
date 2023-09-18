from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemKpisCountEndpoint import SystemKpisCountEndpoint
from pyconnectwise.endpoints.manage.SystemKpisIdEndpoint import SystemKpisIdEndpoint
from pyconnectwise.models.manage import KPI
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemKpisEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "kpis", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemKpisCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemKpisIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemKpisIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemKpisIdEndpoint: The initialized SystemKpisIdEndpoint object.
        """
        child = SystemKpisIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[KPI]:
        """
        Performs a GET request against the /system/kpis endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KPI]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), KPI, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KPI]:
        """
        Performs a GET request against the /system/kpis endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KPI]: The parsed response data.
        """
        return self._parse_many(KPI, super()._make_request("GET", data=data, params=params).json())
