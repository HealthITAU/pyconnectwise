from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdManagementreportnotificationsCountEndpoint import \
    CompanyManagementIdManagementreportnotificationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdManagementreportnotificationsIdEndpoint import \
    CompanyManagementIdManagementreportnotificationsIdEndpoint
from pyconnectwise.models.manage import ManagementReportNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyManagementIdManagementreportnotificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementReportNotifications", parent_endpoint=parent_endpoint)

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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ManagementReportNotification, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ManagementReportNotification]:
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

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagementReportNotification:
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
