from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesInfoTypesEndpoint import (
    CompanyCompaniesInfoTypesEndpoint,
)


class CompanyCompaniesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "info", parent_endpoint=parent_endpoint
        )

        self.types = self._register_child_endpoint(
            CompanyCompaniesInfoTypesEndpoint(client, parent_endpoint=self)
        )
