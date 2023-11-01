from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemPortalreportsCountEndpoint import (
    SystemPortalreportsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemPortalreportsIdEndpoint import (
    SystemPortalreportsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import PortalReport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemPortalreportsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[PortalReport], ConnectWiseManageRequestParams],
    IPostable[PortalReport, ConnectWiseManageRequestParams],
    IPaginateable[PortalReport, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "portalReports", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[PortalReport])
        IPostable.__init__(self, PortalReport)
        IPaginateable.__init__(self, PortalReport)

        self.count = self._register_child_endpoint(
            SystemPortalreportsCountEndpoint(client, parent_endpoint=self)
        )

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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PortalReport,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[PortalReport]:
        """
        Performs a GET request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PortalReport]: The parsed response data.
        """
        return self._parse_many(
            PortalReport, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PortalReport:
        """
        Performs a POST request against the /system/portalReports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PortalReport: The parsed response data.
        """
        return self._parse_one(
            PortalReport, super()._make_request("POST", data=data, params=params).json()
        )
