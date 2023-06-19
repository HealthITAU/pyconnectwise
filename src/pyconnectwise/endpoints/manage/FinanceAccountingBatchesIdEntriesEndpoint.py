from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesIdEndpoint import FinanceAccountingBatchesIdEntriesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesCountEndpoint import FinanceAccountingBatchesIdEntriesCountEndpoint
from pyconnectwise.models.manage.BatchEntryModel import BatchEntryModel

class FinanceAccountingBatchesIdEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingBatchesIdEntriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingBatchesIdEntriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingBatchesIdEntriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingBatchesIdEntriesIdEndpoint: The initialized FinanceAccountingBatchesIdEntriesIdEndpoint object.
        """
        child = FinanceAccountingBatchesIdEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BatchEntryModel]:
        """
        Performs a GET request against the /finance/accounting/batches/{parentId}/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BatchEntryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BatchEntryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BatchEntryModel]:
        """
        Performs a GET request against the /finance/accounting/batches/{parentId}/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BatchEntryModel]: The parsed response data.
        """
        return self._parse_many(BatchEntryModel, super().make_request("GET", params=params).json())
        