from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesCountEndpoint import CompanyCompaniesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesDefaultEndpoint import CompanyCompaniesDefaultEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdEndpoint import CompanyCompaniesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoEndpoint import CompanyCompaniesInfoEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesStatusesEndpoint import CompanyCompaniesStatusesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesTypesEndpoint import CompanyCompaniesTypesEndpoint
from pyconnectwise.models.manage import Company
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companies", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyCompaniesInfoEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(CompanyCompaniesCountEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(CompanyCompaniesTypesEndpoint(client, parent_endpoint=self))
        self.default = self._register_child_endpoint(CompanyCompaniesDefaultEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(CompanyCompaniesStatusesEndpoint(client, parent_endpoint=self))

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

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Company]:
        """
        Performs a GET request against the /company/companies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Company]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Company, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Company]:
        """
        Performs a GET request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Company]: The parsed response data.
        """
        return self._parse_many(Company, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Company:
        """
        Performs a POST request against the /company/companies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(Company, super()._make_request("POST", data=data, params=params).json())
