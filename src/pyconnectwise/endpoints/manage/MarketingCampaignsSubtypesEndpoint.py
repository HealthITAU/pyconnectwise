from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesCountEndpoint import (
    MarketingCampaignsSubtypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesIdEndpoint import MarketingCampaignsSubtypesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import CampaignCampaignSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingCampaignsSubtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CampaignCampaignSubType], ConnectWiseManageRequestParams],
    IPostable[CampaignCampaignSubType, ConnectWiseManageRequestParams],
    IPaginateable[CampaignCampaignSubType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "subTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CampaignCampaignSubType])
        IPostable.__init__(self, CampaignCampaignSubType)
        IPaginateable.__init__(self, CampaignCampaignSubType)

        self.count = self._register_child_endpoint(
            MarketingCampaignsSubtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> MarketingCampaignsSubtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsSubtypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            MarketingCampaignsSubtypesIdEndpoint: The initialized MarketingCampaignsSubtypesIdEndpoint object.
        """
        child = MarketingCampaignsSubtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CampaignCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/subTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CampaignCampaignSubType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CampaignCampaignSubType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CampaignCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CampaignCampaignSubType]: The parsed response data.
        """
        return self._parse_many(CampaignCampaignSubType, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> CampaignCampaignSubType:
        """
        Performs a POST request against the /marketing/campaigns/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CampaignCampaignSubType: The parsed response data.
        """
        return self._parse_one(CampaignCampaignSubType, super()._make_request("POST", data=data, params=params).json())
