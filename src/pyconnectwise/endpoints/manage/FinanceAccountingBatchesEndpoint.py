from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesCountEndpoint import (
    FinanceAccountingBatchesCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingBatchesIdEndpoint import (
    FinanceAccountingBatchesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AccountingBatch, GLExport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class FinanceAccountingBatchesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AccountingBatch], ConnectWiseManageRequestParams],
    IPostable[GLExport, ConnectWiseManageRequestParams],
    IPaginateable[AccountingBatch, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "batches", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AccountingBatch])
        IPostable.__init__(self, GLExport)
        IPaginateable.__init__(self, AccountingBatch)

        self.count = self._register_child_endpoint(
            FinanceAccountingBatchesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAccountingBatchesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingBatchesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingBatchesIdEndpoint: The initialized FinanceAccountingBatchesIdEndpoint object.
        """
        child = FinanceAccountingBatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AccountingBatch]:
        """
        Performs a GET request against the /finance/accounting/batches endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            AccountingBatch,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AccountingBatch]:
        """
        Performs a GET request against the /finance/accounting/batches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingBatch]: The parsed response data.
        """
        return self._parse_many(
            AccountingBatch,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> GLExport:
        """
        Performs a POST request against the /finance/accounting/batches endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLExport: The parsed response data.
        """
        return self._parse_one(
            GLExport, super()._make_request("POST", data=data, params=params).json()
        )
