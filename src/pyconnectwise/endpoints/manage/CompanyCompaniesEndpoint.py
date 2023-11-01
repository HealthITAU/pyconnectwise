from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesCountEndpoint import (
    CompanyCompaniesCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesDefaultEndpoint import (
    CompanyCompaniesDefaultEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesIdEndpoint import (
    CompanyCompaniesIdEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoEndpoint import (
    CompanyCompaniesInfoEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesEndpoint import (
    CompanyCompaniesStatusesEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesEndpoint import (
    CompanyCompaniesTypesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import Company
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class CompanyCompaniesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Company], ConnectWiseManageRequestParams],
    IPostable[Company, ConnectWiseManageRequestParams],
    IPaginateable[Company, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "companies", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Company])
        IPostable.__init__(self, Company)
        IPaginateable.__init__(self, Company)

        self.count = self._register_child_endpoint(
            CompanyCompaniesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            CompanyCompaniesInfoEndpoint(client, parent_endpoint=self)
        )
        self.default = self._register_child_endpoint(
            CompanyCompaniesDefaultEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self._register_child_endpoint(
            CompanyCompaniesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self._register_child_endpoint(
            CompanyCompaniesTypesEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyCompaniesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdEndpoint: The initialized CompanyCompaniesIdEndpoint object.
        """
        child = CompanyCompaniesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Company]:
        """
        Performs a GET request against the /company/companies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Company]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Company,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Company]:
        """
        Performs a GET request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Company]: The parsed response data.
        """
        return self._parse_many(
            Company, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Company:
        """
        Performs a POST request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(
            Company, super()._make_request("POST", data=data, params=params).json()
        )
