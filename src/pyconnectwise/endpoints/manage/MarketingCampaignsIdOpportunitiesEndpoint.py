from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsIdOpportunitiesCountEndpoint import MarketingCampaignsIdOpportunitiesCountEndpoint
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel

class MarketingCampaignsIdOpportunitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdOpportunitiesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityReferenceModel]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/opportunities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityReferenceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityReferenceModel]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityReferenceModel]: The parsed response data.
        """
        return self._parse_many(OpportunityReferenceModel, super().make_request("GET", params=params).json())
        