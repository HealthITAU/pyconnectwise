from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdApplicationparametersIdEndpoint import (
    FinanceAgreementsIdApplicationparametersIdEndpoint,
)


class FinanceAgreementsIdApplicationparametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "applicationParameters", parent_endpoint=parent_endpoint
        )

    def id(
        self, id: int  # noqa: A002
    ) -> FinanceAgreementsIdApplicationparametersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdApplicationparametersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdApplicationparametersIdEndpoint: The initialized FinanceAgreementsIdApplicationparametersIdEndpoint object.
        """
        child = FinanceAgreementsIdApplicationparametersIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child
