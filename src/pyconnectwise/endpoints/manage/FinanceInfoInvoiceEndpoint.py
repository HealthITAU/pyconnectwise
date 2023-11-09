from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoInvoiceIdEndpoint import FinanceInfoInvoiceIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceInfoInvoiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "invoice", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> FinanceInfoInvoiceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceInfoInvoiceIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceInfoInvoiceIdEndpoint: The initialized FinanceInfoInvoiceIdEndpoint object.
        """
        child = FinanceInfoInvoiceIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
