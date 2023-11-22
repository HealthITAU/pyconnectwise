from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanyfinanceIdEndpoint import CompanyCompanyfinanceIdEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyCompanyfinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "companyFinance", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> CompanyCompanyfinanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanyfinanceIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyCompanyfinanceIdEndpoint: The initialized CompanyCompanyfinanceIdEndpoint object.
        """
        child = CompanyCompanyfinanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
