from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsIdEndpoint import MarketingCampaignsIdAuditsIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsCountEndpoint import MarketingCampaignsIdAuditsCountEndpoint
from pyconnectwise.models.manage.CampaignAuditModel import CampaignAuditModel

class MarketingCampaignsIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
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
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignAuditModel]:
        """
        Performs a GET request against the /marketing/campaigns/{parentId}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignAuditModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignAuditModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignAuditModel]:
        """
        Performs a GET request against the /marketing/campaigns/{parentId}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignAuditModel]: The parsed response data.
        """
        return self._parse_many(CampaignAuditModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignAuditModel:
        """
        Performs a POST request against the /marketing/campaigns/{parentId}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignAuditModel: The parsed response data.
        """
        return self._parse_one(CampaignAuditModel, super().make_request("POST", params=params).json())
        