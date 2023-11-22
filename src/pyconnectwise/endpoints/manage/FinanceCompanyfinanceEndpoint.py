from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceCompanyfinanceCountEndpoint import FinanceCompanyfinanceCountEndpoint
from pyconnectwise.endpoints.manage.FinanceCompanyfinanceIdEndpoint import FinanceCompanyfinanceIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceCompanyfinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "companyFinance", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceCompanyfinanceCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> FinanceCompanyfinanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceCompanyfinanceIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            FinanceCompanyfinanceIdEndpoint: The initialized FinanceCompanyfinanceIdEndpoint object.
        """
        child = FinanceCompanyfinanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
