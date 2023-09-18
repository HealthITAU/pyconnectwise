from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesIdAuditsCountEndpoint import ExpenseEntriesIdAuditsCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesIdAuditsIdEndpoint import ExpenseEntriesIdAuditsIdEndpoint
from pyconnectwise.models.manage import ExpenseEntryAudit
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExpenseEntriesIdAuditsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "audits", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ExpenseEntriesIdAuditsCountEndpoint(client, parent_endpoint=self))

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

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ExpenseEntryAudit]:
        """
        Performs a GET request against the /expense/entries/{id}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseEntryAudit]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseEntryAudit, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseEntryAudit]:
        """
        Performs a GET request against the /expense/entries/{id}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseEntryAudit]: The parsed response data.
        """
        return self._parse_many(ExpenseEntryAudit, super()._make_request("GET", data=data, params=params).json())
