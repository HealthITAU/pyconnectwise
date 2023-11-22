from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesIdEndpoint import CompanyEntitytypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyEntitytypesInfoEndpoint import CompanyEntitytypesInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyEntitytypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "entitytypes", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(CompanyEntitytypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> CompanyEntitytypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyEntitytypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            CompanyEntitytypesIdEndpoint: The initialized CompanyEntitytypesIdEndpoint object.
        """
        child = CompanyEntitytypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
