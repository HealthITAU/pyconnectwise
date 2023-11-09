from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdAuditsCountEndpoint import ExpenseReportsIdAuditsCountEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdAuditsIdEndpoint import ExpenseReportsIdAuditsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import ExpenseReportAudit
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ExpenseReportsIdAuditsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ExpenseReportAudit], ConnectWiseManageRequestParams],
    IPaginateable[ExpenseReportAudit, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "audits", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ExpenseReportAudit])
        IPaginateable.__init__(self, ExpenseReportAudit)

        self.count = self._register_child_endpoint(ExpenseReportsIdAuditsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ExpenseReportsIdAuditsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseReportsIdAuditsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ExpenseReportsIdAuditsIdEndpoint: The initialized ExpenseReportsIdAuditsIdEndpoint object.
        """
        child = ExpenseReportsIdAuditsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ExpenseReportAudit]:
        """
        Performs a GET request against the /expense/reports/{id}/audits endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ExpenseReportAudit]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ExpenseReportAudit, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ExpenseReportAudit]:
        """
        Performs a GET request against the /expense/reports/{id}/audits endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ExpenseReportAudit]: The parsed response data.
        """
        return self._parse_many(ExpenseReportAudit, super()._make_request("GET", data=data, params=params).json())
