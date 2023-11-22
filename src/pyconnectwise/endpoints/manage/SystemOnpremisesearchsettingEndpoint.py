from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOnpremisesearchsettingCountEndpoint import (
    SystemOnpremisesearchsettingCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemOnpremisesearchsettingIdEndpoint import (
    SystemOnpremisesearchsettingIdEndpoint,
)


class SystemOnpremisesearchsettingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "onPremiseSearchSetting", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemOnpremisesearchsettingCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemOnpremisesearchsettingIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemOnpremisesearchsettingIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemOnpremisesearchsettingIdEndpoint: The initialized SystemOnpremisesearchsettingIdEndpoint object.
        """
        child = SystemOnpremisesearchsettingIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
