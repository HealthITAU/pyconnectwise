from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembertemplatesCountEndpoint import (
    SystemMembertemplatesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMembertemplatesIdEndpoint import (
    SystemMembertemplatesIdEndpoint,
)


class SystemMembertemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "membertemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemMembertemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembertemplatesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemMembertemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembertemplatesIdEndpoint: The initialized SystemMembertemplatesIdEndpoint object.
        """
        child = SystemMembertemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
