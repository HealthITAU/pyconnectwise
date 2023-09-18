from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncAuthorizeEndpoint import SystemM365contactsyncAuthorizeEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncCheckvalidsyncEndpoint import \
    SystemM365contactsyncCheckvalidsyncEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdEndpoint import SystemM365contactsyncIdEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncInfoEndpoint import SystemM365contactsyncInfoEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncNotifydeactivationEndpoint import \
    SystemM365contactsyncNotifydeactivationEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncNotifyerrorEndpoint import \
    SystemM365contactsyncNotifyerrorEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemM365contactsyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "m365contactsync", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemM365contactsyncInfoEndpoint(client, parent_endpoint=self))
        self.checkvalidsync = self._register_child_endpoint(
            SystemM365contactsyncCheckvalidsyncEndpoint(client, parent_endpoint=self)
        )
        self.authorize = self._register_child_endpoint(
            SystemM365contactsyncAuthorizeEndpoint(client, parent_endpoint=self)
        )
        self.notifyerror = self._register_child_endpoint(
            SystemM365contactsyncNotifyerrorEndpoint(client, parent_endpoint=self)
        )
        self.notifydeactivation = self._register_child_endpoint(
            SystemM365contactsyncNotifydeactivationEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemM365contactsyncIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemM365contactsyncIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemM365contactsyncIdEndpoint: The initialized SystemM365contactsyncIdEndpoint object.
        """
        child = SystemM365contactsyncIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
