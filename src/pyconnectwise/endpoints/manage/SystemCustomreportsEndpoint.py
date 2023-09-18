from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsCountEndpoint import SystemCustomreportsCountEndpoint
from pyconnectwise.endpoints.manage.SystemCustomreportsIdEndpoint import SystemCustomreportsIdEndpoint
from pyconnectwise.models.manage import CustomReport
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemCustomreportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "customReports", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemCustomreportsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemCustomreportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCustomreportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCustomreportsIdEndpoint: The initialized SystemCustomreportsIdEndpoint object.
        """
        child = SystemCustomreportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CustomReport]:
        """
        Performs a GET request against the /system/customReports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CustomReport]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CustomReport, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CustomReport]:
        """
        Performs a GET request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CustomReport]: The parsed response data.
        """
        return self._parse_many(CustomReport, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CustomReport:
        """
        Performs a POST request against the /system/customReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CustomReport: The parsed response data.
        """
        return self._parse_one(CustomReport, super()._make_request("POST", data=data, params=params).json())
