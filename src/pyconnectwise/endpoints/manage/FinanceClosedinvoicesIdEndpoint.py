from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ClosedInvoice
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceClosedinvoicesIdEndpoint(
    ConnectWiseEndpoint,
    IPuttable[ClosedInvoice, ConnectWiseManageRequestParams],
    IPatchable[ClosedInvoice, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPuttable.__init__(self, ClosedInvoice)
        IPatchable.__init__(self, ClosedInvoice)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ClosedInvoice:
        """
        Performs a PUT request against the /finance/closedInvoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ClosedInvoice: The parsed response data.
        """
        return self._parse_one(ClosedInvoice, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ClosedInvoice:
        """
        Performs a PATCH request against the /finance/closedInvoices/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ClosedInvoice: The parsed response data.
        """
        return self._parse_one(ClosedInvoice, super()._make_request("PATCH", data=data, params=params).json())
