from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdInfoEndpoint import (
    CompanyEntitytypesIdInfoEndpoint,
)


class CompanyEntitytypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            CompanyEntitytypesIdInfoEndpoint(client, parent_endpoint=self)
        )
