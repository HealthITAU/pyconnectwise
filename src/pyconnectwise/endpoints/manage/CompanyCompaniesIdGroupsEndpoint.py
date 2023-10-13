from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdGroupsCountEndpoint import CompanyCompaniesIdGroupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdGroupsIdEndpoint import CompanyCompaniesIdGroupsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CompanyGroup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCompaniesIdGroupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyGroup], ConnectWiseManageRequestParams],
    IPostable[CompanyGroup, ConnectWiseManageRequestParams],
    IPaginateable[CompanyGroup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "groups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyGroup])
        IPostable.__init__(self, CompanyGroup)
        IPaginateable.__init__(self, CompanyGroup)

        self.count = self._register_child_endpoint(CompanyCompaniesIdGroupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesIdGroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdGroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdGroupsIdEndpoint: The initialized CompanyCompaniesIdGroupsIdEndpoint object.
        """
        child = CompanyCompaniesIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyGroup]:
        """
        Performs a GET request against the /company/companies/{id}/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyGroup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyGroup, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CompanyGroup]:
        """
        Performs a GET request against the /company/companies/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyGroup]: The parsed response data.
        """
        return self._parse_many(CompanyGroup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyGroup:
        """
        Performs a POST request against the /company/companies/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyGroup: The parsed response data.
        """
        return self._parse_one(CompanyGroup, super()._make_request("POST", data=data, params=params).json())
