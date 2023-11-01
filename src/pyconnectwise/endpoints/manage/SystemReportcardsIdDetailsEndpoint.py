from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemReportcardsIdDetailsCountEndpoint import (
    SystemReportcardsIdDetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemReportcardsIdDetailsIdEndpoint import (
    SystemReportcardsIdDetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ReportCardDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemReportcardsIdDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ReportCardDetail], ConnectWiseManageRequestParams],
    IPostable[ReportCardDetail, ConnectWiseManageRequestParams],
    IPaginateable[ReportCardDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "details", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ReportCardDetail])
        IPostable.__init__(self, ReportCardDetail)
        IPaginateable.__init__(self, ReportCardDetail)

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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ReportCardDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ReportCardDetail]:
        """
        Performs a GET request against the /system/reportCards/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ReportCardDetail]: The parsed response data.
        """
        return self._parse_many(
            ReportCardDetail,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ReportCardDetail:
        """
        Performs a POST request against the /system/reportCards/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ReportCardDetail: The parsed response data.
        """
        return self._parse_one(
            ReportCardDetail,
            super()._make_request("POST", data=data, params=params).json(),
        )
