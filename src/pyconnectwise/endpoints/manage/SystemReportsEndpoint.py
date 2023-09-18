from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportsIdEndpoint import SystemReportsIdEndpoint
from pyconnectwise.models.manage import Report
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemReportsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reports", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemReportsIdEndpoint: The initialized SystemReportsIdEndpoint object.
        """
        child = SystemReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Report]:
        """
        Performs a GET request against the /system/reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Report]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Report, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Report]:
        """
        Performs a GET request against the /system/reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Report]: The parsed response data.
        """
        return self._parse_many(Report, super()._make_request("GET", data=data, params=params).json())
