from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import GLExport
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAccountingExportEndpoint(ConnectWiseEndpoint, IPostable[GLExport, ConnectWiseManageRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "export", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, GLExport)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> GLExport:
        """
        Performs a POST request against the /finance/accounting/export endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLExport: The parsed response data.
        """
        return self._parse_one(GLExport, super()._make_request("POST", data=data, params=params).json())
