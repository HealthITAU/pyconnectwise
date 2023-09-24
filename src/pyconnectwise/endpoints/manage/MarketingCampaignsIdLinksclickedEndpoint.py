from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdLinksclickedCountEndpoint import \
    MarketingCampaignsIdLinksclickedCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdLinksclickedIdEndpoint import \
    MarketingCampaignsIdLinksclickedIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import LinkClicked
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class MarketingCampaignsIdLinksclickedEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LinkClicked], ConnectWiseManageRequestParams],
    IPostable[LinkClicked, ConnectWiseManageRequestParams],
    IPaginateable[LinkClicked, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "linksClicked", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            MarketingCampaignsIdLinksclickedCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsIdLinksclickedIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdLinksclickedIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsIdLinksclickedIdEndpoint: The initialized MarketingCampaignsIdLinksclickedIdEndpoint object.
        """
        child = MarketingCampaignsIdLinksclickedIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[LinkClicked]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/linksClicked endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LinkClicked]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LinkClicked, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[LinkClicked]:
        """
        Performs a GET request against the /marketing/campaigns/{id}/linksClicked endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LinkClicked]: The parsed response data.
        """
        return self._parse_many(LinkClicked, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> LinkClicked:
        """
        Performs a POST request against the /marketing/campaigns/{id}/linksClicked endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LinkClicked: The parsed response data.
        """
        return self._parse_one(LinkClicked, super()._make_request("POST", data=data, params=params).json())
