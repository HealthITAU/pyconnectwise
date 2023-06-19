from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubTypesIdEndpoint import MarketingCampaignsTypesIdSubTypesIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubTypesCountEndpoint import MarketingCampaignsTypesIdSubTypesCountEndpoint
from pyconnectwise.models.manage.CampaignSubTypeModel import CampaignSubTypeModel

class MarketingCampaignsTypesIdSubTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "subTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsTypesIdSubTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> MarketingCampaignsTypesIdSubTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsTypesIdSubTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsTypesIdSubTypesIdEndpoint: The initialized MarketingCampaignsTypesIdSubTypesIdEndpoint object.
        """
        child = MarketingCampaignsTypesIdSubTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignSubTypeModel]:
        """
        Performs a GET request against the /marketing/campaigns/types/{parentId}/subTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignSubTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignSubTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignSubTypeModel]:
        """
        Performs a GET request against the /marketing/campaigns/types/{parentId}/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignSubTypeModel]: The parsed response data.
        """
        return self._parse_many(CampaignSubTypeModel, super().make_request("GET", params=params).json())
        