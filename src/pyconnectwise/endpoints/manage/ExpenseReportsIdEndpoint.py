from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdApproveEndpoint import ExpenseReportsIdApproveEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdAuditsEndpoint import ExpenseReportsIdAuditsEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdRejectEndpoint import ExpenseReportsIdRejectEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdReverseEndpoint import ExpenseReportsIdReverseEndpoint
from pyconnectwise.endpoints.manage.ExpenseReportsIdSubmitEndpoint import ExpenseReportsIdSubmitEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ExpenseReport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ExpenseReportsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ExpenseReport, ConnectWiseManageRequestParams],
    IPaginateable[ExpenseReport, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ExpenseReport)
        IPaginateable.__init__(self, ExpenseReport)

        self.submit = self._register_child_endpoint(ExpenseReportsIdSubmitEndpoint(client, parent_endpoint=self))
        self.audits = self._register_child_endpoint(ExpenseReportsIdAuditsEndpoint(client, parent_endpoint=self))
        self.reject = self._register_child_endpoint(ExpenseReportsIdRejectEndpoint(client, parent_endpoint=self))
        self.approve = self._register_child_endpoint(ExpenseReportsIdApproveEndpoint(client, parent_endpoint=self))
        self.reverse = self._register_child_endpoint(ExpenseReportsIdReverseEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ExpenseReport]:
        """
        Performs a GET request against the /expense/reports/{id} endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params), ExpenseReport, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ExpenseReport:
        """
        Performs a GET request against the /expense/reports/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ExpenseReport: The parsed response data.
        """
        return self._parse_one(ExpenseReport, super()._make_request("GET", data=data, params=params).json())
