from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdInfoEndpoint import (
    ProcurementShipmentmethodsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdUsagesEndpoint import (
    ProcurementShipmentmethodsIdUsagesEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import ShipmentMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementShipmentmethodsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ShipmentMethod, ConnectWiseManageRequestParams],
    IPatchable[ShipmentMethod, ConnectWiseManageRequestParams],
    IPuttable[ShipmentMethod, ConnectWiseManageRequestParams],
    IPaginateable[ShipmentMethod, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ShipmentMethod)
        IPatchable.__init__(self, ShipmentMethod)
        IPuttable.__init__(self, ShipmentMethod)
        IPaginateable.__init__(self, ShipmentMethod)

        self.info = self._register_child_endpoint(
            ProcurementShipmentmethodsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(
            ProcurementShipmentmethodsIdUsagesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ShipmentMethod]:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ShipmentMethod]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ShipmentMethod, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ShipmentMethod:
        """
        Performs a GET request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethod: The parsed response data.
        """
        return self._parse_one(ShipmentMethod, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ShipmentMethod:
        """
        Performs a PATCH request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethod: The parsed response data.
        """
        return self._parse_one(ShipmentMethod, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ShipmentMethod:
        """
        Performs a PUT request against the /procurement/shipmentmethods/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethod: The parsed response data.
        """
        return self._parse_one(ShipmentMethod, super()._make_request("PUT", data=data, params=params).json())
