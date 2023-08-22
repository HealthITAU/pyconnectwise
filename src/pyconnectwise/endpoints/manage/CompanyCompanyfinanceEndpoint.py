from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompanyfinanceIdEndpoint import CompanyCompanyfinanceIdEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompanyfinanceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyFinance", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CompanyCompanyfinanceIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanyfinanceIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompanyfinanceIdEndpoint: The initialized CompanyCompanyfinanceIdEndpoint object.
        """
        child = CompanyCompanyfinanceIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
