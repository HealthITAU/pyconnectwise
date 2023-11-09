from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEmailtemplatesCountEndpoint import (
    ProcurementRmastatusesIdEmailtemplatesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementRmastatusesIdEmailtemplatesIdEndpoint import (
    ProcurementRmastatusesIdEmailtemplatesIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementRmastatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "emailtemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementRmastatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ProcurementRmastatusesIdEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementRmastatusesIdEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ProcurementRmastatusesIdEmailtemplatesIdEndpoint: The initialized ProcurementRmastatusesIdEmailtemplatesIdEndpoint object.
        """
        child = ProcurementRmastatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
