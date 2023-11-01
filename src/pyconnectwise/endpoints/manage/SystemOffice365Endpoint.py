from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOffice365EmailsetupsEndpoint import (
    SystemOffice365EmailsetupsEndpoint,
)


class SystemOffice365Endpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "office365", parent_endpoint=parent_endpoint
        )

        self.email_setups = self._register_child_endpoint(
            SystemOffice365EmailsetupsEndpoint(client, parent_endpoint=self)
        )
