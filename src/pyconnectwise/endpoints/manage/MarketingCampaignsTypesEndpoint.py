from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesCountEndpoint import MarketingCampaignsTypesCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdEndpoint import MarketingCampaignsTypesIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesInfoEndpoint import MarketingCampaignsTypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CampaignType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class MarketingCampaignsTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CampaignType], ConnectWiseManageRequestParams],
    IPostable[CampaignType, ConnectWiseManageRequestParams],
    IPaginateable[CampaignType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CampaignType])
        IPostable.__init__(self, CampaignType)
        IPaginateable.__init__(self, CampaignType)

        self.count = self._register_child_endpoint(MarketingCampaignsTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(MarketingCampaignsTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> MarketingCampaignsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsTypesIdEndpoint: The initialized MarketingCampaignsTypesIdEndpoint object.
        """
        child = MarketingCampaignsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CampaignType]:
        """
        Performs a GET request against the /marketing/campaigns/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CampaignType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[CampaignType]:
        """
        Performs a GET request against the /marketing/campaigns/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignType]: The parsed response data.
        """
        return self._parse_many(CampaignType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CampaignType:
        """
        Performs a POST request against the /marketing/campaigns/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignType: The parsed response data.
        """
        return self._parse_one(CampaignType, super()._make_request("POST", data=data, params=params).json())
