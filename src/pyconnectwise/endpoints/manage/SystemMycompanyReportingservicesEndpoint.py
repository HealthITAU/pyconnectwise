from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyReportingservicesIdEndpoint import \
    SystemMycompanyReportingservicesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ReportingService
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMycompanyReportingservicesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ReportingService], ConnectWiseManageRequestParams],
    IPaginateable[ReportingService, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "reportingServices", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ReportingService])
        IPaginateable.__init__(self, ReportingService)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ReportingService, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ReportingService]:
        """
        Performs a GET request against the /system/mycompany/reportingServices endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportingService]: The parsed response data.
        """
        return self._parse_many(ReportingService, super()._make_request("GET", data=data, params=params).json())
