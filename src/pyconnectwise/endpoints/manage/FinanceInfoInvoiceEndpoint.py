from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceInfoInvoiceIdEndpoint import (
    FinanceInfoInvoiceIdEndpoint,
)


class FinanceInfoInvoiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "invoice", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> FinanceInfoInvoiceIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceInfoInvoiceIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceInfoInvoiceIdEndpoint: The initialized FinanceInfoInvoiceIdEndpoint object.
        """
        child = FinanceInfoInvoiceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
