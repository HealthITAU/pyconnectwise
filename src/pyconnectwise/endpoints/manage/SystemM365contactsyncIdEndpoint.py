from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdInfoEndpoint import SystemM365contactsyncIdInfoEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdTestEndpoint import SystemM365contactsyncIdTestEndpoint
from pyconnectwise.endpoints.manage.SystemM365contactsyncIdViewauthEndpoint import \
    SystemM365contactsyncIdViewauthEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemM365contactsyncIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(SystemM365contactsyncIdInfoEndpoint(client, parent_endpoint=self))
        self.viewauth = self._register_child_endpoint(
            SystemM365contactsyncIdViewauthEndpoint(client, parent_endpoint=self)
        )
        self.test = self._register_child_endpoint(SystemM365contactsyncIdTestEndpoint(client, parent_endpoint=self))
