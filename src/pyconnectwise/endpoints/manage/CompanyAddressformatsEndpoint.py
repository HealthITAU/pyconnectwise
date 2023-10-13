from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsCountEndpoint import CompanyAddressformatsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsIdEndpoint import CompanyAddressformatsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyAddressformatsInfoEndpoint import CompanyAddressformatsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AddressFormat
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyAddressformatsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AddressFormat], ConnectWiseManageRequestParams],
    IPostable[AddressFormat, ConnectWiseManageRequestParams],
    IPaginateable[AddressFormat, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "addressFormats", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AddressFormat])
        IPostable.__init__(self, AddressFormat)
        IPaginateable.__init__(self, AddressFormat)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AddressFormat, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[AddressFormat]:
        """
        Performs a GET request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AddressFormat]: The parsed response data.
        """
        return self._parse_many(AddressFormat, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AddressFormat:
        """
        Performs a POST request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AddressFormat: The parsed response data.
        """
        return self._parse_one(AddressFormat, super()._make_request("POST", data=data, params=params).json())
