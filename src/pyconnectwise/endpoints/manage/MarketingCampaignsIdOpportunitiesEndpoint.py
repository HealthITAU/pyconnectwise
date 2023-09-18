from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdOpportunitiesCountEndpoint import \
    MarketingCampaignsIdOpportunitiesCountEndpoint
from pyconnectwise.models.manage import OpportunityReference
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsIdOpportunitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsIdOpportunitiesCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OpportunityReference]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/opportunities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityReference]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), OpportunityReference, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityReference]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityReference]: The parsed response data.
        """
        return self._parse_many(OpportunityReference, super()._make_request("GET", data=data, params=params).json())
