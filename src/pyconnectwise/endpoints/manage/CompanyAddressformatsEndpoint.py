from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsCountEndpoint import CompanyAddressformatsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsIdEndpoint import CompanyAddressformatsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsInfoEndpoint import CompanyAddressformatsInfoEndpoint
from pyconnectwise.models.manage import AddressFormat
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyAddressformatsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "addressFormats", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyAddressformatsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyAddressformatsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyAddressformatsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyAddressformatsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyAddressformatsIdEndpoint: The initialized CompanyAddressformatsIdEndpoint object.
        """
        child = CompanyAddressformatsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[AddressFormat]:
        """
        Performs a GET request against the /company/addressFormats endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AddressFormat]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), AddressFormat, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AddressFormat]:
        """
        Performs a GET request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AddressFormat]: The parsed response data.
        """
        return self._parse_many(AddressFormat, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AddressFormat:
        """
        Performs a POST request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AddressFormat: The parsed response data.
        """
        return self._parse_one(AddressFormat, super()._make_request("POST", data=data, params=params).json())
