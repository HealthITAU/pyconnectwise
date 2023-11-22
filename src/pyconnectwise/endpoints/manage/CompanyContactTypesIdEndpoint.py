from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactTypesIdUsagesEndpoint import (
    CompanyContactTypesIdUsagesEndpoint,
)


class CompanyContactTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.usages = self._register_child_endpoint(CompanyContactTypesIdUsagesEndpoint(client, parent_endpoint=self))
