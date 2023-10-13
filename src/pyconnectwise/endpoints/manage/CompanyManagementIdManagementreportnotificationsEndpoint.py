from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdManagementreportnotificationsCountEndpoint import \
    CompanyManagementIdManagementreportnotificationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdManagementreportnotificationsIdEndpoint import \
    CompanyManagementIdManagementreportnotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ManagementReportNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyManagementIdManagementreportnotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ManagementReportNotification], ConnectWiseManageRequestParams],
    IPostable[ManagementReportNotification, ConnectWiseManageRequestParams],
    IPaginateable[ManagementReportNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "managementReportNotifications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ManagementReportNotification])
        IPostable.__init__(self, ManagementReportNotification)
        IPaginateable.__init__(self, ManagementReportNotification)

        self.count = self._register_child_endpoint(
            CompanyManagementIdManagementreportnotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyManagementIdManagementreportnotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyManagementIdManagementreportnotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyManagementIdManagementreportnotificationsIdEndpoint: The initialized CompanyManagementIdManagementreportnotificationsIdEndpoint object.
        """
        child = CompanyManagementIdManagementreportnotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ManagementReportNotification]:
        """
        Performs a GET request against the /company/management/{id}/managementReportNotifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementReportNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementReportNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ManagementReportNotification]:
        """
        Performs a GET request against the /company/management/{id}/managementReportNotifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementReportNotification]: The parsed response data.
        """
        return self._parse_many(
            ManagementReportNotification, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementReportNotification:
        """
        Performs a POST request against the /company/management/{id}/managementReportNotifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportNotification: The parsed response data.
        """
        return self._parse_one(
            ManagementReportNotification, super()._make_request("POST", data=data, params=params).json()
        )
