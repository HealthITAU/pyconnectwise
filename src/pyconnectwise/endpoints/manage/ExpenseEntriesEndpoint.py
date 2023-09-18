from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesCountEndpoint import ExpenseEntriesCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseEntriesIdEndpoint import ExpenseEntriesIdEndpoint
from pyconnectwise.models.manage import ExpenseEntry
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ExpenseEntriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entries", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ExpenseEntriesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ExpenseEntriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseEntriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseEntriesIdEndpoint: The initialized ExpenseEntriesIdEndpoint object.
        """
        child = ExpenseEntriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ExpenseEntry]:
        """
        Performs a GET request against the /expense/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseEntry]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseEntry, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ExpenseEntry]:
        """
        Performs a GET request against the /expense/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseEntry]: The parsed response data.
        """
        return self._parse_many(ExpenseEntry, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ExpenseEntry:
        """
        Performs a POST request against the /expense/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseEntry: The parsed response data.
        """
        return self._parse_one(ExpenseEntry, super()._make_request("POST", data=data, params=params).json())
