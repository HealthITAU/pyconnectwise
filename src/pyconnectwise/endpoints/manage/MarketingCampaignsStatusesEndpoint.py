from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesIdEndpoint import MarketingCampaignsStatusesIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesCountEndpoint import MarketingCampaignsStatusesCountEndpoint
from pyconnectwise.models.manage.CampaignStatusModel import CampaignStatusModel

class MarketingCampaignsStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignStatusModel]:
        """
        Performs a GET request against the /marketing/campaigns/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignStatusModel]:
        """
        Performs a GET request against the /marketing/campaigns/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignStatusModel]: The parsed response data.
        """
        return self._parse_many(CampaignStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignStatusModel:
        """
        Performs a POST request against the /marketing/campaigns/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignStatusModel: The parsed response data.
        """
        return self._parse_one(CampaignStatusModel, super().make_request("POST", params=params).json())
        