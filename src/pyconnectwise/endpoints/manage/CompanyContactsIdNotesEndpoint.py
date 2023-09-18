from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesCountEndpoint import CompanyContactsIdNotesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdNotesIdEndpoint import CompanyContactsIdNotesIdEndpoint
from pyconnectwise.models.manage import ContactNote
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyContactsIdNotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdNotesIdEndpoint: The initialized CompanyContactsIdNotesIdEndpoint object.
        """
        child = CompanyContactsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactNote]:
        """
        Performs a GET request against the /company/contacts/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactNote]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactNote, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactNote]:
        """
        Performs a GET request against the /company/contacts/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactNote]: The parsed response data.
        """
        return self._parse_many(ContactNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactNote:
        """
        Performs a POST request against the /company/contacts/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactNote: The parsed response data.
        """
        return self._parse_one(ContactNote, super()._make_request("POST", data=data, params=params).json())
