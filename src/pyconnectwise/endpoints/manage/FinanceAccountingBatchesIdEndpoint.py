from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesEndpoint import (
    FinanceAccountingBatchesIdEntriesEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdExportEndpoint import (
    FinanceAccountingBatchesIdExportEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import AccountingBatch
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceAccountingBatchesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[AccountingBatch, ConnectWiseManageRequestParams],
    IPaginateable[AccountingBatch, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, AccountingBatch)
        IPaginateable.__init__(self, AccountingBatch)

        self.entries = self._register_child_endpoint(
            FinanceAccountingBatchesIdEntriesEndpoint(client, parent_endpoint=self)
        )
        self.export = self._register_child_endpoint(
            FinanceAccountingBatchesIdExportEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AccountingBatch]:
        """
        Performs a GET request against the /finance/accounting/batches/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingBatch]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AccountingBatch, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /finance/accounting/batches/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AccountingBatch:
        """
        Performs a GET request against the /finance/accounting/batches/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AccountingBatch: The parsed response data.
        """
        return self._parse_one(AccountingBatch, super()._make_request("GET", data=data, params=params).json())
