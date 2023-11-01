from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesCountEndpoint import (
    CompanyCompaniesStatusesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesIdEndpoint import (
    CompanyCompaniesStatusesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import CompanyStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCompaniesStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyStatus], ConnectWiseManageRequestParams],
    IPostable[CompanyStatus, ConnectWiseManageRequestParams],
    IPaginateable[CompanyStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "statuses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[CompanyStatus])
        IPostable.__init__(self, CompanyStatus)
        IPaginateable.__init__(self, CompanyStatus)

        self.count = self._register_child_endpoint(
            CompanyCompaniesStatusesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesStatusesIdEndpoint: The initialized CompanyCompaniesStatusesIdEndpoint object.
        """
        child = CompanyCompaniesStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CompanyStatus]:
        """
        Performs a GET request against the /company/companies/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CompanyStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[CompanyStatus]:
        """
        Performs a GET request against the /company/companies/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyStatus]: The parsed response data.
        """
        return self._parse_many(
            CompanyStatus, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CompanyStatus:
        """
        Performs a POST request against the /company/companies/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyStatus: The parsed response data.
        """
        return self._parse_one(
            CompanyStatus,
            super()._make_request("POST", data=data, params=params).json(),
        )
