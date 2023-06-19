from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsOpenedIdEndpoint import MarketingCampaignsIdEmailsOpenedIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEmailsOpenedCountEndpoint import MarketingCampaignsIdEmailsOpenedCountEndpoint
from pyconnectwise.models.manage.EmailOpenedModel import EmailOpenedModel

class MarketingCampaignsIdEmailsOpenedEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailsOpened", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingCampaignsIdEmailsOpenedCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> MarketingCampaignsIdEmailsOpenedIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdEmailsOpenedIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdEmailsOpenedIdEndpoint: The initialized MarketingCampaignsIdEmailsOpenedIdEndpoint object.
        """
        child = MarketingCampaignsIdEmailsOpenedIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[EmailOpenedModel]:
        """
        Performs a GET request against the /marketing/campaigns/{parentId}/emailsOpened endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailOpenedModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            EmailOpenedModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EmailOpenedModel]:
        """
        Performs a GET request against the /marketing/campaigns/{parentId}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailOpenedModel]: The parsed response data.
        """
        return self._parse_many(EmailOpenedModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EmailOpenedModel:
        """
        Performs a POST request against the /marketing/campaigns/{parentId}/emailsOpened endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailOpenedModel: The parsed response data.
        """
        return self._parse_one(EmailOpenedModel, super().make_request("POST", params=params).json())
        