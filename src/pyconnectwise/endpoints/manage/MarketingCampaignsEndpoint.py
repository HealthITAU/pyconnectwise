from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsCountEndpoint import MarketingCampaignsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEndpoint import MarketingCampaignsIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesEndpoint import MarketingCampaignsStatusesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesEndpoint import MarketingCampaignsSubtypesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesEndpoint import MarketingCampaignsTypesEndpoint
from pyconnectwise.models.manage import Campaign
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "campaigns", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(MarketingCampaignsCountEndpoint(client, parent_endpoint=self))
        self.sub_types = self._register_child_endpoint(MarketingCampaignsSubtypesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(MarketingCampaignsTypesEndpoint(client, parent_endpoint=self))
        self.statuses = self._register_child_endpoint(MarketingCampaignsStatusesEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> MarketingCampaignsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdEndpoint: The initialized MarketingCampaignsIdEndpoint object.
        """
        child = MarketingCampaignsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Campaign]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Campaign, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Campaign]: The parsed response data.
        """
        return self._parse_many(Campaign, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Campaign:
        """
        Performs a POST request against the /marketing/campaigns endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("POST", data=data, params=params).json())
