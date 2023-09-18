from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdCompaniesEndpoint import MarketingGroupsIdCompaniesEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsEndpoint import MarketingGroupsIdContactsEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdInfoEndpoint import MarketingGroupsIdInfoEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdUsagesEndpoint import MarketingGroupsIdUsagesEndpoint
from pyconnectwise.models.manage import Group
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingGroupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.companies = self._register_child_endpoint(MarketingGroupsIdCompaniesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(MarketingGroupsIdInfoEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(MarketingGroupsIdUsagesEndpoint(client, parent_endpoint=self))
        self.contacts = self._register_child_endpoint(MarketingGroupsIdContactsEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Group]:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Group]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Group, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Group:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(Group, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Group:
        """
        Performs a PUT request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(Group, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Group:
        """
        Performs a PATCH request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Group: The parsed response data.
        """
        return self._parse_one(Group, super()._make_request("PATCH", data=data, params=params).json())
