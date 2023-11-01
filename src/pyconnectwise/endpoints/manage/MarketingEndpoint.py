from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsEndpoint import (
    MarketingCampaignsEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingGroupsEndpoint import (
    MarketingGroupsEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class MarketingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "marketing", parent_endpoint=parent_endpoint
        )

        self.campaigns = self._register_child_endpoint(
            MarketingCampaignsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self._register_child_endpoint(
            MarketingGroupsEndpoint(client, parent_endpoint=self)
        )
