from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingPackageSetupIdEndpoint import FinanceAccountingPackageSetupIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingPackageSetupCountEndpoint import FinanceAccountingPackageSetupCountEndpoint
from pyconnectwise.models.manage.AccountingPackageSetupModel import AccountingPackageSetupModel

class FinanceAccountingPackageSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackageSetup", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingPackageSetupCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingPackageSetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingPackageSetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingPackageSetupIdEndpoint: The initialized FinanceAccountingPackageSetupIdEndpoint object.
        """
        child = FinanceAccountingPackageSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AccountingPackageSetupModel]:
        """
        Performs a GET request against the /finance/accountingPackageSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingPackageSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AccountingPackageSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AccountingPackageSetupModel]:
        """
        Performs a GET request against the /finance/accountingPackageSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingPackageSetupModel]: The parsed response data.
        """
        return self._parse_many(AccountingPackageSetupModel, super().make_request("GET", params=params).json())
        