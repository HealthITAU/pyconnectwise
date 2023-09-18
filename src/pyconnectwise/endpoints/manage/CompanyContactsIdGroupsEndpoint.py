from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsCountEndpoint import CompanyContactsIdGroupsCountEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdGroupsIdEndpoint import CompanyContactsIdGroupsIdEndpoint
from pyconnectwise.models.manage import ContactGroup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyContactsIdGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(CompanyContactsIdGroupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyContactsIdGroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdGroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdGroupsIdEndpoint: The initialized CompanyContactsIdGroupsIdEndpoint object.
        """
        child = CompanyContactsIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ContactGroup]:
        """
        Performs a GET request against the /company/contacts/{id}/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactGroup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ContactGroup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactGroup]:
        """
        Performs a GET request against the /company/contacts/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactGroup]: The parsed response data.
        """
        return self._parse_many(ContactGroup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactGroup:
        """
        Performs a POST request against the /company/contacts/{id}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactGroup: The parsed response data.
        """
        return self._parse_one(ContactGroup, super()._make_request("POST", data=data, params=params).json())
