from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersIdOptionsEndpoint import (
    SystemWorkflowsIdTriggersIdOptionsEndpoint,
)


class SystemWorkflowsIdTriggersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.options = self._register_child_endpoint(
            SystemWorkflowsIdTriggersIdOptionsEndpoint(client, parent_endpoint=self)
        )
