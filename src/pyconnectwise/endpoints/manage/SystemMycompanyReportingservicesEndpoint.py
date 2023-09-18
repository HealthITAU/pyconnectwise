from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyReportingservicesIdEndpoint import \
    SystemMycompanyReportingservicesIdEndpoint
from pyconnectwise.models.manage import ReportingService
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyReportingservicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "reportingServices", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemMycompanyReportingservicesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyReportingservicesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyReportingservicesIdEndpoint: The initialized SystemMycompanyReportingservicesIdEndpoint object.
        """
        child = SystemMycompanyReportingservicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ReportingService]:
        """
        Performs a GET request against the /system/mycompany/reportingServices endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportingService]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ReportingService, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ReportingService]:
        """
        Performs a GET request against the /system/mycompany/reportingServices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportingService]: The parsed response data.
        """
        return self._parse_many(ReportingService, super()._make_request("GET", data=data, params=params).json())
