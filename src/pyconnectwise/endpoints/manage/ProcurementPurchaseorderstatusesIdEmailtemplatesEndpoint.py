from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint import \
    ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint import \
    ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementPurchaseorderstatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailtemplates", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesIdEmailtemplatesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint: The initialized ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint object.
        """
        child = ProcurementPurchaseorderstatusesIdEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
