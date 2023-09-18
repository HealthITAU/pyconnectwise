from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesCountEndpoint import CompanyCompaniesIdNotesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesIdEndpoint import CompanyCompaniesIdNotesIdEndpoint
from pyconnectwise.models.manage import CompanyNote
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyCompaniesIdNotesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCompaniesIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdNotesIdEndpoint: The initialized CompanyCompaniesIdNotesIdEndpoint object.
        """
        child = CompanyCompaniesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyNote]:
        """
        Performs a GET request against the /company/companies/{id}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyNote]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CompanyNote, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyNote]:
        """
        Performs a GET request against the /company/companies/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyNote]: The parsed response data.
        """
        return self._parse_many(CompanyNote, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyNote:
        """
        Performs a POST request against the /company/companies/{id}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyNote: The parsed response data.
        """
        return self._parse_one(CompanyNote, super()._make_request("POST", data=data, params=params).json())
