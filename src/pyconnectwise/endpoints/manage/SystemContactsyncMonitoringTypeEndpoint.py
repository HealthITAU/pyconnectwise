from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringTypeIdEndpoint import (
    SystemContactsyncMonitoringTypeIdEndpoint,
)


class SystemContactsyncMonitoringTypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "type", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemContactsyncMonitoringTypeIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemContactsyncMonitoringTypeIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemContactsyncMonitoringTypeIdEndpoint: The initialized SystemContactsyncMonitoringTypeIdEndpoint object.
        """
        child = SystemContactsyncMonitoringTypeIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
