from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesCountEndpoint import CompanyCountriesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesIdEndpoint import CompanyCountriesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCountriesInfoEndpoint import CompanyCountriesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Country
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyCountriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Country], ConnectWiseManageRequestParams],
    IPostable[Country, ConnectWiseManageRequestParams],
    IPaginateable[Country, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "countries", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Country])
        IPostable.__init__(self, Country)
        IPaginateable.__init__(self, Country)

        self.count = self._register_child_endpoint(CompanyCountriesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyCountriesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> CompanyCountriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCountriesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyCountriesIdEndpoint: The initialized CompanyCountriesIdEndpoint object.
        """
        child = CompanyCountriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Country]:
        """
        Performs a GET request against the /company/countries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Country]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Country, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Country]:
        """
        Performs a GET request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Country]: The parsed response data.
        """
        return self._parse_many(Country, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Country:
        """
        Performs a POST request against the /company/countries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Country: The parsed response data.
        """
        return self._parse_one(Country, super()._make_request("POST", data=data, params=params).json())
