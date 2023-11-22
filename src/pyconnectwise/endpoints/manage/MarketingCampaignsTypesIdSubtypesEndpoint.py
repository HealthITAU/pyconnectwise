from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubtypesCountEndpoint import (
    MarketingCampaignsTypesIdSubtypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubtypesIdEndpoint import (
    MarketingCampaignsTypesIdSubtypesIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import TypeCampaignSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingCampaignsTypesIdSubtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TypeCampaignSubType], ConnectWiseManageRequestParams],
    IPaginateable[TypeCampaignSubType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "subTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[TypeCampaignSubType])
        IPaginateable.__init__(self, TypeCampaignSubType)

        self.count = self._register_child_endpoint(
            MarketingCampaignsTypesIdSubtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> MarketingCampaignsTypesIdSubtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsTypesIdSubtypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            MarketingCampaignsTypesIdSubtypesIdEndpoint: The initialized MarketingCampaignsTypesIdSubtypesIdEndpoint object.
        """
        child = MarketingCampaignsTypesIdSubtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[TypeCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/types/{id}/subTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TypeCampaignSubType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), TypeCampaignSubType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[TypeCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/types/{id}/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TypeCampaignSubType]: The parsed response data.
        """
        return self._parse_many(TypeCampaignSubType, super()._make_request("GET", data=data, params=params).json())
