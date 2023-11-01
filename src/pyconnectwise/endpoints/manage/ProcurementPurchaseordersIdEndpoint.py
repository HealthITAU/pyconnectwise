from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdLineitemsEndpoint import (
    ProcurementPurchaseordersIdLineitemsEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdRebatchEndpoint import (
    ProcurementPurchaseordersIdRebatchEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdUnbatchEndpoint import (
    ProcurementPurchaseordersIdUnbatchEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import PurchaseOrder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementPurchaseordersIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[PurchaseOrder, ConnectWiseManageRequestParams],
    IPuttable[PurchaseOrder, ConnectWiseManageRequestParams],
    IPatchable[PurchaseOrder, ConnectWiseManageRequestParams],
    IPaginateable[PurchaseOrder, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, PurchaseOrder)
        IPuttable.__init__(self, PurchaseOrder)
        IPatchable.__init__(self, PurchaseOrder)
        IPaginateable.__init__(self, PurchaseOrder)

        self.rebatch = self._register_child_endpoint(
            ProcurementPurchaseordersIdRebatchEndpoint(client, parent_endpoint=self)
        )
        self.lineitems = self._register_child_endpoint(
            ProcurementPurchaseordersIdLineitemsEndpoint(client, parent_endpoint=self)
        )
        self.unbatch = self._register_child_endpoint(
            ProcurementPurchaseordersIdUnbatchEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[PurchaseOrder]:
        """
        Performs a GET request against the /procurement/purchaseorders/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrder]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            PurchaseOrder,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrder:
        """
        Performs a GET request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrder, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrder:
        """
        Performs a PUT request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrder, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PurchaseOrder:
        """
        Performs a PATCH request against the /procurement/purchaseorders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrder: The parsed response data.
        """
        return self._parse_one(
            PurchaseOrder,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
