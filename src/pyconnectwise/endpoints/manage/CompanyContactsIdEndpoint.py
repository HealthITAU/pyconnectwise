from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsEndpoint import \
    CompanyContactsIdCommunicationsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsEndpoint import CompanyContactsIdGroupsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdImageEndpoint import CompanyContactsIdImageEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesEndpoint import CompanyContactsIdNotesEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdPortalsecurityEndpoint import \
    CompanyContactsIdPortalsecurityEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTracksEndpoint import CompanyContactsIdTracksEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdTypeassociationsEndpoint import \
    CompanyContactsIdTypeassociationsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdUsagesEndpoint import CompanyContactsIdUsagesEndpoint
from pyconnectwise.models.manage import Contact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.groups = self._register_child_endpoint(CompanyContactsIdGroupsEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(CompanyContactsIdUsagesEndpoint(client, parent_endpoint=self))
        self.communications = self._register_child_endpoint(
            CompanyContactsIdCommunicationsEndpoint(client, parent_endpoint=self)
        )
        self.image = self._register_child_endpoint(CompanyContactsIdImageEndpoint(client, parent_endpoint=self))
        self.tracks = self._register_child_endpoint(CompanyContactsIdTracksEndpoint(client, parent_endpoint=self))
        self.notes = self._register_child_endpoint(CompanyContactsIdNotesEndpoint(client, parent_endpoint=self))
        self.portal_security = self._register_child_endpoint(
            CompanyContactsIdPortalsecurityEndpoint(client, parent_endpoint=self)
        )
        self.type_associations = self._register_child_endpoint(
            CompanyContactsIdTypeassociationsEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Contact]:
        """
        Performs a GET request against the /company/contacts/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Contact]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Contact, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Contact:
        """
        Performs a GET request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(Contact, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Contact:
        """
        Performs a PUT request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(Contact, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Contact:
        """
        Performs a PATCH request against the /company/contacts/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(Contact, super()._make_request("PATCH", data=data, params=params).json())
