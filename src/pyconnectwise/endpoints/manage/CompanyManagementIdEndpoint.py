from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdExecutemanageditsyncEndpoint import \
    CompanyManagementIdExecutemanageditsyncEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdLogEndpoint import CompanyManagementIdLogEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdLogsEndpoint import CompanyManagementIdLogsEndpoint
from pyconnectwise.endpoints.manage.CompanyManagementIdManagementreportnotificationsEndpoint import \
    CompanyManagementIdManagementreportnotificationsEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Management
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyManagementIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Management, ConnectWiseManageRequestParams],
    IPuttable[Management, ConnectWiseManageRequestParams],
    IPatchable[Management, ConnectWiseManageRequestParams],
    IPaginateable[Management, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Management)
        IPuttable.__init__(self, Management)
        IPatchable.__init__(self, Management)
        IPaginateable.__init__(self, Management)

        self.execute_managed_it_sync = self._register_child_endpoint(
            CompanyManagementIdExecutemanageditsyncEndpoint(client, parent_endpoint=self)
        )
        self.logs = self._register_child_endpoint(CompanyManagementIdLogsEndpoint(client, parent_endpoint=self))
        self.management_report_notifications = self._register_child_endpoint(
            CompanyManagementIdManagementreportnotificationsEndpoint(client, parent_endpoint=self)
        )
        self.log = self._register_child_endpoint(CompanyManagementIdLogEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Management]:
        """
        Performs a GET request against the /company/management/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Management]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Management, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Management:
        """
        Performs a GET request against the /company/management/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Management: The parsed response data.
        """
        return self._parse_one(Management, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Management:
        """
        Performs a PUT request against the /company/management/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Management: The parsed response data.
        """
        return self._parse_one(Management, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Management:
        """
        Performs a PATCH request against the /company/management/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Management: The parsed response data.
        """
        return self._parse_one(Management, super()._make_request("PATCH", data=data, params=params).json())
