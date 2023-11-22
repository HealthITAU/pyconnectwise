from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesCountEndpoint import ProcurementSubcategoriesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesIdEndpoint import ProcurementSubcategoriesIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesInfoEndpoint import ProcurementSubcategoriesInfoEndpoint

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementSubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "subcategories", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementSubcategoriesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementSubcategoriesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ProcurementSubcategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementSubcategoriesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementSubcategoriesIdEndpoint: The initialized ProcurementSubcategoriesIdEndpoint object.
        """
        child = ProcurementSubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
