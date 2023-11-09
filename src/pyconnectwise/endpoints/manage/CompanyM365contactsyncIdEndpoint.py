from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyM365contactsyncIdPropertyEndpoint import (
    CompanyM365contactsyncIdPropertyEndpoint,
)


class CompanyM365contactsyncIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.property = self._register_child_endpoint(
            CompanyM365contactsyncIdPropertyEndpoint(client, parent_endpoint=self)
        )
