from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdInfoEndpoint import ProcurementWarehousebinsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsIdInventoryonhandEndpoint import \
    ProcurementWarehousebinsIdInventoryonhandEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import WarehouseBin
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ProcurementWarehousebinsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[WarehouseBin, ConnectWiseManageRequestParams],
    IPuttable[WarehouseBin, ConnectWiseManageRequestParams],
    IPatchable[WarehouseBin, ConnectWiseManageRequestParams],
    IPaginateable[WarehouseBin, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, WarehouseBin)
        IPuttable.__init__(self, WarehouseBin)
        IPatchable.__init__(self, WarehouseBin)
        IPaginateable.__init__(self, WarehouseBin)

        self.inventory_on_hand = self._register_child_endpoint(
            ProcurementWarehousebinsIdInventoryonhandEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementWarehousebinsIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[WarehouseBin]:
        """
        Performs a GET request against the /procurement/warehouseBins/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WarehouseBin]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), WarehouseBin, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WarehouseBin:
        """
        Performs a GET request against the /procurement/warehouseBins/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBin: The parsed response data.
        """
        return self._parse_one(WarehouseBin, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /procurement/warehouseBins/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> WarehouseBin:
        """
        Performs a PUT request against the /procurement/warehouseBins/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBin: The parsed response data.
        """
        return self._parse_one(WarehouseBin, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> WarehouseBin:
        """
        Performs a PATCH request against the /procurement/warehouseBins/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBin: The parsed response data.
        """
        return self._parse_one(WarehouseBin, super()._make_request("PATCH", data=data, params=params).json())
