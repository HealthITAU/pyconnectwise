from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportsIdColumnsEndpoint import SystemReportsIdColumnsEndpoint
from pyconnectwise.endpoints.manage.SystemReportsIdCountEndpoint import SystemReportsIdCountEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import ReportDataResponse
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemReportsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ReportDataResponse, ConnectWiseManageRequestParams],
    IPaginateable[ReportDataResponse, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ReportDataResponse)
        IPaginateable.__init__(self, ReportDataResponse)

        self.columns = self._register_child_endpoint(SystemReportsIdColumnsEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(SystemReportsIdCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ReportDataResponse]:
        """
        Performs a GET request against the /system/reports/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ReportDataResponse]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ReportDataResponse, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ReportDataResponse:
        """
        Performs a GET request against the /system/reports/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportDataResponse: The parsed response data.
        """
        return self._parse_one(ReportDataResponse, super()._make_request("GET", data=data, params=params).json())
