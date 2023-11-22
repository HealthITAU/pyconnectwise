from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdEndpoint import FinanceAgreementtypesIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceAgreementtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "agreementTypes", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> FinanceAgreementtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdEndpoint: The initialized FinanceAgreementtypesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
