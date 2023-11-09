from pyconnectwise.endpoints.automate.LocationsIdProbeconfigurationEndpoint import (
    LocationsIdProbeconfigurationEndpoint,
)
from pyconnectwise.endpoints.automate.LocationsIdUpgradeprobeEndpoint import (
    LocationsIdUpgradeprobeEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class LocationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.probeconfiguration = self._register_child_endpoint(
            LocationsIdProbeconfigurationEndpoint(client, parent_endpoint=self)
        )
        self.upgradeprobe = self._register_child_endpoint(LocationsIdUpgradeprobeEndpoint(client, parent_endpoint=self))
