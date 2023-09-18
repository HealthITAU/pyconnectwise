from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsCountEndpoint import MarketingGroupsIdContactsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsIdEndpoint import MarketingGroupsIdContactsIdEndpoint
from pyconnectwise.models.manage import MarketingContact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingGroupsIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(MarketingGroupsIdContactsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> MarketingGroupsIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingGroupsIdContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingGroupsIdContactsIdEndpoint: The initialized MarketingGroupsIdContactsIdEndpoint object.
        """
        child = MarketingGroupsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MarketingContact]:
        """
        Performs a GET request against the /marketing/groups/{id}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketingContact]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MarketingContact, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MarketingContact]:
        """
        Performs a GET request against the /marketing/groups/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketingContact]: The parsed response data.
        """
        return self._parse_many(MarketingContact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MarketingContact:
        """
        Performs a POST request against the /marketing/groups/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketingContact: The parsed response data.
        """
        return self._parse_one(MarketingContact, super()._make_request("POST", data=data, params=params).json())
