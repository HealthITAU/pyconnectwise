from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsCountEndpoint import CompanyCompaniesIdTeamsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsIdEndpoint import CompanyCompaniesIdTeamsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import CompanyTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyCompaniesIdTeamsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CompanyTeam], ConnectWiseManageRequestParams],
    IPostable[CompanyTeam, ConnectWiseManageRequestParams],
    IPaginateable[CompanyTeam, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "teams", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CompanyTeam])
        IPostable.__init__(self, CompanyTeam)
        IPaginateable.__init__(self, CompanyTeam)

        self.count = self._register_child_endpoint(CompanyCompaniesIdTeamsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> CompanyCompaniesIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTeamsIdEndpoint: The initialized CompanyCompaniesIdTeamsIdEndpoint object.
        """
        child = CompanyCompaniesIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CompanyTeam]:
        """
        Performs a GET request against the /company/companies/{id}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTeam]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyTeam, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CompanyTeam]:
        """
        Performs a GET request against the /company/companies/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTeam]: The parsed response data.
        """
        return self._parse_many(CompanyTeam, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CompanyTeam:
        """
        Performs a POST request against the /company/companies/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyTeam: The parsed response data.
        """
        return self._parse_one(CompanyTeam, super()._make_request("POST", data=data, params=params).json())
