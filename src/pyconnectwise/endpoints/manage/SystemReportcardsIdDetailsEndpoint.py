from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsIdDetailsCountEndpoint import \
    SystemReportcardsIdDetailsCountEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsIdDetailsIdEndpoint import SystemReportcardsIdDetailsIdEndpoint
from pyconnectwise.models.manage import ReportCardDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemReportcardsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemReportcardsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemReportcardsIdDetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemReportcardsIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemReportcardsIdDetailsIdEndpoint: The initialized SystemReportcardsIdDetailsIdEndpoint object.
        """
        child = SystemReportcardsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ReportCardDetail]:
        """
        Performs a GET request against the /system/reportCards/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportCardDetail]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ReportCardDetail, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ReportCardDetail]:
        """
        Performs a GET request against the /system/reportCards/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportCardDetail]: The parsed response data.
        """
        return self._parse_many(ReportCardDetail, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ReportCardDetail:
        """
        Performs a POST request against the /system/reportCards/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCardDetail: The parsed response data.
        """
        return self._parse_one(ReportCardDetail, super()._make_request("POST", data=data, params=params).json())
