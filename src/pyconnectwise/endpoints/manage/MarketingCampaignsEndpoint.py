from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsCountEndpoint import MarketingCampaignsCountEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsIdEndpoint import MarketingCampaignsIdEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsStatusesEndpoint import MarketingCampaignsStatusesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsSubtypesEndpoint import MarketingCampaignsSubtypesEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesEndpoint import MarketingCampaignsTypesEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Campaign
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class MarketingCampaignsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Campaign], ConnectWiseManageRequestParams],
    IPostable[Campaign, ConnectWiseManageRequestParams],
    IPaginateable[Campaign, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "campaigns", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Campaign])
        IPostable.__init__(self, Campaign)
        IPaginateable.__init__(self, Campaign)

        self.statuses = self._register_child_endpoint(MarketingCampaignsStatusesEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(MarketingCampaignsTypesEndpoint(client, parent_endpoint=self))
        self.sub_types = self._register_child_endpoint(MarketingCampaignsSubtypesEndpoint(client, parent_endpoint=self))
        self.count = self._register_child_endpoint(MarketingCampaignsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> MarketingCampaignsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            MarketingCampaignsIdEndpoint: The initialized MarketingCampaignsIdEndpoint object.
        """
        child = MarketingCampaignsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Campaign]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Campaign, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Campaign]:
        """
        Performs a GET request against the /marketing/campaigns endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Campaign]: The parsed response data.
        """
        return self._parse_many(Campaign, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Campaign:
        """
        Performs a POST request against the /marketing/campaigns endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Campaign: The parsed response data.
        """
        return self._parse_one(Campaign, super()._make_request("POST", data=data, params=params).json())
