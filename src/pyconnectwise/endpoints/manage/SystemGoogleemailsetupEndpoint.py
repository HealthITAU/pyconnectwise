from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupCountEndpoint import SystemGoogleemailsetupCountEndpoint
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupIdEndpoint import SystemGoogleemailsetupIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemGoogleemailsetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "googleemailsetup", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemGoogleemailsetupCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemGoogleemailsetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemGoogleemailsetupIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemGoogleemailsetupIdEndpoint: The initialized SystemGoogleemailsetupIdEndpoint object.
        """
        child = SystemGoogleemailsetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
