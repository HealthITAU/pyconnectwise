from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementrecapIdEndpoint import (
    FinanceAgreementrecapIdEndpoint,
)


class FinanceAgreementrecapEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "agreementrecap", parent_endpoint=parent_endpoint
        )

    def id(self, id: int) -> FinanceAgreementrecapIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementrecapIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementrecapIdEndpoint: The initialized FinanceAgreementrecapIdEndpoint object.
        """
        child = FinanceAgreementrecapIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
