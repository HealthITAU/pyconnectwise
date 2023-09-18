from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsCountEndpoint import \
    CompanyContactsRelationshipsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsRelationshipsIdEndpoint import CompanyContactsRelationshipsIdEndpoint
from pyconnectwise.models.manage import ContactRelationship
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsRelationshipsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "relationships", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyContactsRelationshipsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsRelationshipsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsRelationshipsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsRelationshipsIdEndpoint: The initialized CompanyContactsRelationshipsIdEndpoint object.
        """
        child = CompanyContactsRelationshipsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ContactRelationship]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactRelationship]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactRelationship, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactRelationship]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactRelationship]: The parsed response data.
        """
        return self._parse_many(ContactRelationship, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactRelationship:
        """
        Performs a POST request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactRelationship: The parsed response data.
        """
        return self._parse_one(ContactRelationship, super()._make_request("POST", data=data, params=params).json())
