from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsEndpoint import MarketingCampaignsEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsEndpoint import MarketingGroupsEndpoint

class MarketingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "marketing")
        
        self.campaigns = self.register_child_endpoint(
            MarketingCampaignsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            MarketingGroupsEndpoint(client, parent_endpoint=self)
        )