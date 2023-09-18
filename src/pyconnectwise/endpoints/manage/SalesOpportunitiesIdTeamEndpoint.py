from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamCountEndpoint import SalesOpportunitiesIdTeamCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamIdEndpoint import SalesOpportunitiesIdTeamIdEndpoint
from pyconnectwise.models.manage import Team
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdTeamEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "team", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOpportunitiesIdTeamCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesIdTeamIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdTeamIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdTeamIdEndpoint: The initialized SalesOpportunitiesIdTeamIdEndpoint object.
        """
        child = SalesOpportunitiesIdTeamIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Team]:
        """
        Performs a GET request against the /sales/opportunities/{id}/team endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Team]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Team, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Team]:
        """
        Performs a GET request against the /sales/opportunities/{id}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Team]: The parsed response data.
        """
        return self._parse_many(Team, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Team:
        """
        Performs a POST request against the /sales/opportunities/{id}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Team: The parsed response data.
        """
        return self._parse_one(Team, super()._make_request("POST", data=data, params=params).json())
