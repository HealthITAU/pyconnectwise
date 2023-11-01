from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowactionsIdAutomateparametersEndpoint import (
    SystemWorkflowactionsIdAutomateparametersEndpoint,
)


class SystemWorkflowactionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.automate_parameters = self._register_child_endpoint(
            SystemWorkflowactionsIdAutomateparametersEndpoint(
                client, parent_endpoint=self
            )
        )
