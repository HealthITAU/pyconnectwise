from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesCountEndpoint import \
    FinanceAccountingUnpostedexpensesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdEndpoint import \
    FinanceAccountingUnpostedexpensesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import UnpostedExpense
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAccountingUnpostedexpensesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnpostedExpense], ConnectWiseManageRequestParams],
    IPaginateable[UnpostedExpense, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "unpostedexpenses", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[UnpostedExpense])
        IPaginateable.__init__(self, UnpostedExpense)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedexpensesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedexpensesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedexpensesIdEndpoint: The initialized FinanceAccountingUnpostedexpensesIdEndpoint object.
        """
        child = FinanceAccountingUnpostedexpensesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[UnpostedExpense]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpense]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), UnpostedExpense, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[UnpostedExpense]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedExpense]: The parsed response data.
        """
        return self._parse_many(UnpostedExpense, super()._make_request("GET", data=data, params=params).json())
