from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceCompanyfinanceCountEndpoint import FinanceCompanyfinanceCountEndpoint
from pyconnectwise.endpoints.manage.FinanceCompanyfinanceIdEndpoint import FinanceCompanyfinanceIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceCompanyfinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyFinance", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceCompanyfinanceCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceCompanyfinanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceCompanyfinanceIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceCompanyfinanceIdEndpoint: The initialized FinanceCompanyfinanceIdEndpoint object.
        """
        child = FinanceCompanyfinanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
