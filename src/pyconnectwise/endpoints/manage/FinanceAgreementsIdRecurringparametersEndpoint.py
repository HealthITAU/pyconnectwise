from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdRecurringparametersIdEndpoint import (
    FinanceAgreementsIdRecurringparametersIdEndpoint,
)


class FinanceAgreementsIdRecurringparametersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "recurringParameters", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> FinanceAgreementsIdRecurringparametersIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdRecurringparametersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdRecurringparametersIdEndpoint: The initialized FinanceAgreementsIdRecurringparametersIdEndpoint object.
        """
        child = FinanceAgreementsIdRecurringparametersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
