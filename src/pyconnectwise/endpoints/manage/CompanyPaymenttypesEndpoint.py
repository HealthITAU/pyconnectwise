from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyPaymenttypesInfoEndpoint import CompanyPaymenttypesInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyPaymenttypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "paymentTypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyPaymenttypesInfoEndpoint(client, parent_endpoint=self))
