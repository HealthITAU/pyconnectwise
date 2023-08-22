from typing import Any

from pyconnectwise.endpoints.automate.LocationsIdProbeconfigurationEndpoint import LocationsIdProbeconfigurationEndpoint
from pyconnectwise.endpoints.automate.LocationsIdUpgradeprobeEndpoint import LocationsIdUpgradeprobeEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class LocationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.upgradeprobe = self._register_child_endpoint(LocationsIdUpgradeprobeEndpoint(client, parent_endpoint=self))
        self.probeconfiguration = self._register_child_endpoint(
            LocationsIdProbeconfigurationEndpoint(client, parent_endpoint=self)
        )
