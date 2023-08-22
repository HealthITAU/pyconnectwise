from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringTypeIdEndpoint import \
    SystemContactsyncMonitoringTypeIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemContactsyncMonitoringTypeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "type", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemContactsyncMonitoringTypeIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemContactsyncMonitoringTypeIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemContactsyncMonitoringTypeIdEndpoint: The initialized SystemContactsyncMonitoringTypeIdEndpoint object.
        """
        child = SystemContactsyncMonitoringTypeIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
