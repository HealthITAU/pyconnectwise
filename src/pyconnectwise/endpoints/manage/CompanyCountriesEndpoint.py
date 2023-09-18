from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesCountEndpoint import CompanyCountriesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesIdEndpoint import CompanyCountriesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesInfoEndpoint import CompanyCountriesInfoEndpoint
from pyconnectwise.models.manage import Country
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCountriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "countries", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyCountriesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyCountriesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCountriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCountriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCountriesIdEndpoint: The initialized CompanyCountriesIdEndpoint object.
        """
        child = CompanyCountriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Country]:
        """
        Performs a GET request against the /company/countries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Country]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Country, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Country]:
        """
        Performs a GET request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Country]: The parsed response data.
        """
        return self._parse_many(Country, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Country:
        """
        Performs a POST request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Country: The parsed response data.
        """
        return self._parse_one(Country, super()._make_request("POST", data=data, params=params).json())
