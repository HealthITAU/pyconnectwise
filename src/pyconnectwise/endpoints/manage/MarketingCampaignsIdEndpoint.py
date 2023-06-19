from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsIdActivitiesEndpoint import MarketingCampaignsIdActivitiesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdOpportunitiesEndpoint import MarketingCampaignsIdOpportunitiesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdAuditsEndpoint import MarketingCampaignsIdAuditsEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsOpenedEndpoint import MarketingCampaignsIdEmailsOpenedEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdFormsSubmittedEndpoint import MarketingCampaignsIdFormsSubmittedEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdLinksClickedEndpoint import MarketingCampaignsIdLinksClickedEndpoint
from pyconnectwise.models.manage.CampaignModel import CampaignModel

class MarketingCampaignsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.activities = self.register_child_endpoint(
            MarketingCampaignsIdActivitiesEndpoint(client, parent_endpoint=self)
        )
        self.opportunities = self.register_child_endpoint(
            MarketingCampaignsIdOpportunitiesEndpoint(client, parent_endpoint=self)
        )
        self.audits = self.register_child_endpoint(
            MarketingCampaignsIdAuditsEndpoint(client, parent_endpoint=self)
        )
        self.emailsOpened = self.register_child_endpoint(
            MarketingCampaignsIdEmailsOpenedEndpoint(client, parent_endpoint=self)
        )
        self.formsSubmitted = self.register_child_endpoint(
            MarketingCampaignsIdFormsSubmittedEndpoint(client, parent_endpoint=self)
        )
        self.linksClicked = self.register_child_endpoint(
            MarketingCampaignsIdLinksClickedEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CampaignModel]:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CampaignModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignModel:
        """
        Performs a GET request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignModel: The parsed response data.
        """
        return self._parse_one(CampaignModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignModel:
        """
        Performs a PUT request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignModel: The parsed response data.
        """
        return self._parse_one(CampaignModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignModel:
        """
        Performs a PATCH request against the /marketing/campaigns/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignModel: The parsed response data.
        """
        return self._parse_one(CampaignModel, super().make_request("PATCH", params=params).json())
        