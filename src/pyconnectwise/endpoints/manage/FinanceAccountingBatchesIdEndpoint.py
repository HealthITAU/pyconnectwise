from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdExportEndpoint import FinanceAccountingBatchesIdExportEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesEndpoint import FinanceAccountingBatchesIdEntriesEndpoint
from pyconnectwise.models.manage.AccountingBatchModel import AccountingBatchModel

class FinanceAccountingBatchesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.export = self.register_child_endpoint(
            FinanceAccountingBatchesIdExportEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            FinanceAccountingBatchesIdEntriesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AccountingBatchModel]:
        """
        Performs a GET request against the /finance/accounting/batches/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingBatchModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AccountingBatchModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AccountingBatchModel:
        """
        Performs a GET request against the /finance/accounting/batches/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AccountingBatchModel: The parsed response data.
        """
        return self._parse_one(AccountingBatchModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /finance/accounting/batches/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        