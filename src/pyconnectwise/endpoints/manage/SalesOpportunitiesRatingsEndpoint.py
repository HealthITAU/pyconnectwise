from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsCountEndpoint import SalesOpportunitiesRatingsCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsIdEndpoint import SalesOpportunitiesRatingsIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsInfoEndpoint import SalesOpportunitiesRatingsInfoEndpoint
from pyconnectwise.models.manage import OpportunityRating
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesRatingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ratings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOpportunitiesRatingsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesOpportunitiesRatingsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesOpportunitiesRatingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesRatingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesRatingsIdEndpoint: The initialized SalesOpportunitiesRatingsIdEndpoint object.
        """
        child = SalesOpportunitiesRatingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityRating]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityRating]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityRating, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityRating]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityRating]: The parsed response data.
        """
        return self._parse_many(OpportunityRating, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityRating:
        """
        Performs a POST request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityRating: The parsed response data.
        """
        return self._parse_one(OpportunityRating, super()._make_request("POST", data=data, params=params).json())
