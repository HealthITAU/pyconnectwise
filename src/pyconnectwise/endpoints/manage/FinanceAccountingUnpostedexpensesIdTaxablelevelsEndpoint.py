from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdTaxablelevelsCountEndpoint import \
    FinanceAccountingUnpostedexpensesIdTaxablelevelsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint import \
    FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import UnpostedExpenseTaxableLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAccountingUnpostedexpensesIdTaxablelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnpostedExpenseTaxableLevel], ConnectWiseManageRequestParams],
    IPaginateable[UnpostedExpenseTaxableLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "taxableLevels", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[UnpostedExpenseTaxableLevel])
        IPaginateable.__init__(self, UnpostedExpenseTaxableLevel)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedexpensesIdTaxablelevelsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint: The initialized FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint object.
        """
        child = FinanceAccountingUnpostedexpensesIdTaxablelevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[UnpostedExpenseTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{id}/taxableLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedExpenseTaxableLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), UnpostedExpenseTaxableLevel, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[UnpostedExpenseTaxableLevel]:
        """
        Performs a GET request against the /finance/accounting/unpostedexpenses/{id}/taxableLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedExpenseTaxableLevel]: The parsed response data.
        """
        return self._parse_many(
            UnpostedExpenseTaxableLevel, super()._make_request("GET", data=data, params=params).json()
        )
