from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ExpenseEntriesIdAuditsIdEndpoint import ExpenseEntriesIdAuditsIdEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesIdAuditsCountEndpoint import ExpenseEntriesIdAuditsCountEndpoint
from pyconnectwise.models.manage.ExpenseEntryAuditModel import ExpenseEntryAuditModel

class ExpenseEntriesIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseEntriesIdAuditsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ExpenseEntriesIdAuditsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseEntriesIdAuditsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseEntriesIdAuditsIdEndpoint: The initialized ExpenseEntriesIdAuditsIdEndpoint object.
        """
        child = ExpenseEntriesIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ExpenseEntryAuditModel]:
        """
        Performs a GET request against the /expense/entries/{parentId}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseEntryAuditModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ExpenseEntryAuditModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseEntryAuditModel]:
        """
        Performs a GET request against the /expense/entries/{parentId}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseEntryAuditModel]: The parsed response data.
        """
        return self._parse_many(ExpenseEntryAuditModel, super().make_request("GET", params=params).json())
        