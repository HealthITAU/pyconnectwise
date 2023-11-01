from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPaymenttypesInfoEndpoint import (
    CompanyPaymenttypesInfoEndpoint,
)


class CompanyPaymenttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "paymentTypes", parent_endpoint=parent_endpoint
        )

        self.info = self._register_child_endpoint(
            CompanyPaymenttypesInfoEndpoint(client, parent_endpoint=self)
        )
