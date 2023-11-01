from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesCountEndpoint import (
    FinanceAccountingBatchesIdEntriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEntriesIdEndpoint import (
    FinanceAccountingBatchesIdEntriesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import BatchEntry
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceAccountingBatchesIdEntriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BatchEntry], ConnectWiseManageRequestParams],
    IPaginateable[BatchEntry, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "entries", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BatchEntry])
        IPaginateable.__init__(self, BatchEntry)

        self.count = self._register_child_endpoint(
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
        child = FinanceAccountingBatchesIdEntriesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BatchEntry]:
        """
        Performs a GET request against the /finance/accounting/batches/{id}/entries endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BatchEntry]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BatchEntry,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BatchEntry]:
        """
        Performs a GET request against the /finance/accounting/batches/{id}/entries endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BatchEntry]: The parsed response data.
        """
        return self._parse_many(
            BatchEntry, super()._make_request("GET", data=data, params=params).json()
        )
