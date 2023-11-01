from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdEndpoint import (
    SystemMyaccountIdEndpoint,
)


class SystemMyaccountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "myAccount", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> SystemMyaccountIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemMyaccountIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyaccountIdEndpoint: The initialized SystemMyaccountIdEndpoint object.
        """
        child = SystemMyaccountIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
