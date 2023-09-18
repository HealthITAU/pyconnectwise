from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemPortalreportsCountEndpoint import SystemPortalreportsCountEndpoint
from pyconnectwise.endpoints.manage.SystemPortalreportsIdEndpoint import SystemPortalreportsIdEndpoint
from pyconnectwise.models.manage import PortalReport
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemPortalreportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalReports", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemPortalreportsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemPortalreportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemPortalreportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemPortalreportsIdEndpoint: The initialized SystemPortalreportsIdEndpoint object.
        """
        child = SystemPortalreportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[PortalReport]:
        """
        Performs a GET request against the /system/portalReports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PortalReport]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), PortalReport, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PortalReport]:
        """
        Performs a GET request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalReport]: The parsed response data.
        """
        return self._parse_many(PortalReport, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PortalReport:
        """
        Performs a POST request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalReport: The parsed response data.
        """
        return self._parse_one(PortalReport, super()._make_request("POST", data=data, params=params).json())
