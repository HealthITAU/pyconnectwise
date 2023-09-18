from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesCountEndpoint import \
    MarketingCampaignsStatusesCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesIdEndpoint import MarketingCampaignsStatusesIdEndpoint
from pyconnectwise.models.manage import CampaignStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsStatusesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsStatusesIdEndpoint: The initialized MarketingCampaignsStatusesIdEndpoint object.
        """
        child = MarketingCampaignsStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CampaignStatus]:
        """
        Performs a GET request against the /marketing/campaigns/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignStatus]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CampaignStatus, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignStatus]:
        """
        Performs a GET request against the /marketing/campaigns/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignStatus]: The parsed response data.
        """
        return self._parse_many(CampaignStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignStatus:
        """
        Performs a POST request against the /marketing/campaigns/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignStatus: The parsed response data.
        """
        return self._parse_one(CampaignStatus, super()._make_request("POST", data=data, params=params).json())
