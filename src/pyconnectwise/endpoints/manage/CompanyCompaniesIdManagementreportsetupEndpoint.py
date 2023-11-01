from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementreportsetupIdEndpoint import (
    CompanyCompaniesIdManagementreportsetupIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ManagementReportSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCompaniesIdManagementreportsetupEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ManagementReportSetup], ConnectWiseManageRequestParams],
    IPostable[ManagementReportSetup, ConnectWiseManageRequestParams],
    IPaginateable[ManagementReportSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "managementReportSetup", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ManagementReportSetup])
        IPostable.__init__(self, ManagementReportSetup)
        IPaginateable.__init__(self, ManagementReportSetup)

    def id(self, id: int) -> CompanyCompaniesIdManagementreportsetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdManagementreportsetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdManagementreportsetupIdEndpoint: The initialized CompanyCompaniesIdManagementreportsetupIdEndpoint object.
        """
        child = CompanyCompaniesIdManagementreportsetupIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ManagementReportSetup]:
        """
        Performs a GET request against the /company/companies/{id}/managementReportSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagementReportSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ManagementReportSetup,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ManagementReportSetup]:
        """
        Performs a GET request against the /company/companies/{id}/managementReportSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ManagementReportSetup]: The parsed response data.
        """
        return self._parse_many(
            ManagementReportSetup,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ManagementReportSetup:
        """
        Performs a POST request against the /company/companies/{id}/managementReportSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetup: The parsed response data.
        """
        return self._parse_one(
            ManagementReportSetup,
            super()._make_request("POST", data=data, params=params).json(),
        )
