from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdUsagesListEndpoint import (
    CompanyContactTypesIdUsagesListEndpoint,
)


class CompanyContactTypesIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "usages", parent_endpoint=parent_endpoint
        )

        self.list = self._register_child_endpoint(
            CompanyContactTypesIdUsagesListEndpoint(client, parent_endpoint=self)
        )
