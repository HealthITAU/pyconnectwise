from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesCountEndpoint import CompanyCompaniesIdSitesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesIdEndpoint import CompanyCompaniesIdSitesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanySite
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompaniesIdSitesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanySite], ConnectWiseManageRequestParams],
    IPostable[CompanySite, ConnectWiseManageRequestParams],
    IPaginateable[CompanySite, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "sites", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanySite])
        IPostable.__init__(self, CompanySite)
        IPaginateable.__init__(self, CompanySite)

        self.count = self._register_child_endpoint(CompanyCompaniesIdSitesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesIdSitesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdSitesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdSitesIdEndpoint: The initialized CompanyCompaniesIdSitesIdEndpoint object.
        """
        child = CompanyCompaniesIdSitesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanySite]:
        """
        Performs a GET request against the /company/companies/{id}/sites endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanySite]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanySite, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CompanySite]:
        """
        Performs a GET request against the /company/companies/{id}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanySite]: The parsed response data.
        """
        return self._parse_many(CompanySite, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanySite:
        """
        Performs a POST request against the /company/companies/{id}/sites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanySite: The parsed response data.
        """
        return self._parse_one(CompanySite, super()._make_request("POST", data=data, params=params).json())
