from typing import Any

from pyconnectwise.endpoints.automate.MonitorsIdCollecteddataEndpoint import MonitorsIdCollecteddataEndpoint
from pyconnectwise.endpoints.automate.MonitorsIdDatacollectionsettingsEndpoint import \
    MonitorsIdDatacollectionsettingsEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class MonitorsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.collecteddata = self._register_child_endpoint(
            MonitorsIdCollecteddataEndpoint(client, parent_endpoint=self)
        )
        self.datacollectionsettings = self._register_child_endpoint(
            MonitorsIdDatacollectionsettingsEndpoint(client, parent_endpoint=self)
        )
