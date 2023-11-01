from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsCountEndpoint import (
    ExpenseReportsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ExpenseReportsIdEndpoint import (
    ExpenseReportsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ExpenseReport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ExpenseReportsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ExpenseReport], ConnectWiseManageRequestParams],
    IPaginateable[ExpenseReport, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "reports", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ExpenseReport])
        IPaginateable.__init__(self, ExpenseReport)

        self.count = self._register_child_endpoint(
            ExpenseReportsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ExpenseReportsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseReportsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseReportsIdEndpoint: The initialized ExpenseReportsIdEndpoint object.
        """
        child = ExpenseReportsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ExpenseReport]:
        """
        Performs a GET request against the /expense/reports endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseReport]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ExpenseReport,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ExpenseReport]:
        """
        Performs a GET request against the /expense/reports endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseReport]: The parsed response data.
        """
        return self._parse_many(
            ExpenseReport, super()._make_request("GET", data=data, params=params).json()
        )
