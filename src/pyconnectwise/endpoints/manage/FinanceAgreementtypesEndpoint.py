from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdEndpoint import FinanceAgreementtypesIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "agreementTypes", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> FinanceAgreementtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementtypesIdEndpoint: The initialized FinanceAgreementtypesIdEndpoint object.
        """
        child = FinanceAgreementtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
