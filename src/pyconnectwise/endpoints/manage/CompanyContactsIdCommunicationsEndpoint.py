from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsCountEndpoint import \
    CompanyContactsIdCommunicationsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsIdEndpoint import \
    CompanyContactsIdCommunicationsIdEndpoint
from pyconnectwise.models.manage import ContactCommunication
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdCommunicationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            CompanyContactsIdCommunicationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsIdCommunicationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdCommunicationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdCommunicationsIdEndpoint: The initialized CompanyContactsIdCommunicationsIdEndpoint object.
        """
        child = CompanyContactsIdCommunicationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ContactCommunication]:
        """
        Performs a GET request against the /company/contacts/{id}/communications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactCommunication]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactCommunication, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactCommunication]:
        """
        Performs a GET request against the /company/contacts/{id}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactCommunication]: The parsed response data.
        """
        return self._parse_many(ContactCommunication, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactCommunication:
        """
        Performs a POST request against the /company/contacts/{id}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactCommunication: The parsed response data.
        """
        return self._parse_one(ContactCommunication, super()._make_request("POST", data=data, params=params).json())
