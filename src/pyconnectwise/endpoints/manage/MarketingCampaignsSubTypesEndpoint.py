from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesCountEndpoint import \
    MarketingCampaignsSubtypesCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesIdEndpoint import MarketingCampaignsSubtypesIdEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage.Campaign.SubType import CampaignSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingCampaignsSubtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "subTypes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsSubtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsSubtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsSubtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsSubtypesIdEndpoint: The initialized MarketingCampaignsSubtypesIdEndpoint object.
        """
        child = MarketingCampaignsSubtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/subTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignSubType]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CampaignSubType,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignSubType]: The parsed response data.
        """
        return self._parse_many(CampaignSubType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CampaignSubType:
        """
        Performs a POST request against the /marketing/campaigns/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignSubType: The parsed response data.
        """
        return self._parse_one(CampaignSubType, super()._make_request("POST", data=data, params=params).json())
