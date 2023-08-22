from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsEndpoint import MarketingCampaignsEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsEndpoint import MarketingGroupsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MarketingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "marketing", parent_endpoint=parent_endpoint)

        self.campaigns = self._register_child_endpoint(MarketingCampaignsEndpoint(client, parent_endpoint=self))
        self.groups = self._register_child_endpoint(MarketingGroupsEndpoint(client, parent_endpoint=self))
