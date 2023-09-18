from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsCountEndpoint import \
    MarketingCampaignsIdAuditsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsIdEndpoint import MarketingCampaignsIdAuditsIdEndpoint
from pyconnectwise.models.manage import CampaignAudit
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsIdAuditsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsIdAuditsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdAuditsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdAuditsIdEndpoint: The initialized MarketingCampaignsIdAuditsIdEndpoint object.
        """
        child = MarketingCampaignsIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CampaignAudit]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignAudit]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CampaignAudit, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignAudit]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignAudit]: The parsed response data.
        """
        return self._parse_many(CampaignAudit, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignAudit:
        """
        Performs a POST request against the /marketing/campaigns/{id}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignAudit: The parsed response data.
        """
        return self._parse_one(CampaignAudit, super()._make_request("POST", data=data, params=params).json())
