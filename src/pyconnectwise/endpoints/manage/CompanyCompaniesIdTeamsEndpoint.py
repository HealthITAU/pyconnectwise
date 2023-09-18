from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsCountEndpoint import CompanyCompaniesIdTeamsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsIdEndpoint import CompanyCompaniesIdTeamsIdEndpoint
from pyconnectwise.models.manage import CompanyTeam
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyCompaniesIdTeamsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTeamsIdEndpoint: The initialized CompanyCompaniesIdTeamsIdEndpoint object.
        """
        child = CompanyCompaniesIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyTeam]:
        """
        Performs a GET request against the /company/companies/{id}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTeam]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyTeam, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyTeam]:
        """
        Performs a GET request against the /company/companies/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTeam]: The parsed response data.
        """
        return self._parse_many(CompanyTeam, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyTeam:
        """
        Performs a POST request against the /company/companies/{id}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyTeam: The parsed response data.
        """
        return self._parse_one(CompanyTeam, super()._make_request("POST", data=data, params=params).json())
