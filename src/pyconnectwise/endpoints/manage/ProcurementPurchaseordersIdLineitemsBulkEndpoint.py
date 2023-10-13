from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BulkResult
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementPurchaseordersIdLineitemsBulkEndpoint(
    ConnectWiseEndpoint,
    IPostable[BulkResult, ConnectWiseManageRequestParams],
    IDeleteable[ConnectWiseManageRequestParams],
    IPuttable[BulkResult, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "bulk", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, BulkResult)
        IDeleteable.__init__(self, None)
        IPuttable.__init__(self, BulkResult)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a POST request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("POST", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a DELETE request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("DELETE", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BulkResult:
        """
        Performs a PUT request against the /procurement/purchaseorders/{id}/lineitems/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("PUT", data=data, params=params).json())
