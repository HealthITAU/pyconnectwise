from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesEndpoint import (
    CompanyContactTypesEndpoint,
)


class CompanyContactEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "contact", parent_endpoint=parent_endpoint
        )

        self.types = self._register_child_endpoint(
            CompanyContactTypesEndpoint(client, parent_endpoint=self)
        )
