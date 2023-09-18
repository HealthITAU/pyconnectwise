from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsCountEndpoint import CompanyContactsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDefaultEndpoint import CompanyContactsDefaultEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsDepartmentsEndpoint import CompanyContactsDepartmentsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdEndpoint import CompanyContactsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsEndpoint import CompanyContactsRelationshipsEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRequestpasswordEndpoint import CompanyContactsRequestpasswordEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsTypesEndpoint import CompanyContactsTypesEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsValidateportalcredentialsEndpoint import \
    CompanyContactsValidateportalcredentialsEndpoint
from pyconnectwise.models.manage import Contact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)

        self.validate_portal_credentials = self._register_child_endpoint(
            CompanyContactsValidateportalcredentialsEndpoint(client, parent_endpoint=self)
        )
        self.departments = self._register_child_endpoint(
            CompanyContactsDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.request_password = self._register_child_endpoint(
            CompanyContactsRequestpasswordEndpoint(client, parent_endpoint=self)
        )
        self.count = self._register_child_endpoint(CompanyContactsCountEndpoint(client, parent_endpoint=self))
        self.default = self._register_child_endpoint(CompanyContactsDefaultEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(CompanyContactsTypesEndpoint(client, parent_endpoint=self))
        self.relationships = self._register_child_endpoint(
            CompanyContactsRelationshipsEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdEndpoint: The initialized CompanyContactsIdEndpoint object.
        """
        child = CompanyContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Contact]:
        """
        Performs a GET request against the /company/contacts endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Contact]:
        """
        Performs a GET request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Contact]: The parsed response data.
        """
        return self._parse_many(Contact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Contact:
        """
        Performs a POST request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Contact: The parsed response data.
        """
        return self._parse_one(Contact, super()._make_request("POST", data=data, params=params).json())
