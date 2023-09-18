from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsCountEndpoint import \
    SalesOpportunitiesIdContactsCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsIdEndpoint import SalesOpportunitiesIdContactsIdEndpoint
from pyconnectwise.models.manage import OpportunityContact
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SalesOpportunitiesIdContactsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesOpportunitiesIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdContactsIdEndpoint: The initialized SalesOpportunitiesIdContactsIdEndpoint object.
        """
        child = SalesOpportunitiesIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityContact]:
        """
        Performs a GET request against the /sales/opportunities/{id}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityContact]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityContact, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityContact]:
        """
        Performs a GET request against the /sales/opportunities/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityContact]: The parsed response data.
        """
        return self._parse_many(OpportunityContact, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityContact:
        """
        Performs a POST request against the /sales/opportunities/{id}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityContact: The parsed response data.
        """
        return self._parse_one(OpportunityContact, super()._make_request("POST", data=data, params=params).json())
