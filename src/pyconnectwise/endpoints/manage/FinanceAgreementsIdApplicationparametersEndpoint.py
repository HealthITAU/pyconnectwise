from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdApplicationparametersIdEndpoint import \
    FinanceAgreementsIdApplicationparametersIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementsIdApplicationparametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "applicationParameters", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> FinanceAgreementsIdApplicationparametersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdApplicationparametersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdApplicationparametersIdEndpoint: The initialized FinanceAgreementsIdApplicationparametersIdEndpoint object.
        """
        child = FinanceAgreementsIdApplicationparametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
