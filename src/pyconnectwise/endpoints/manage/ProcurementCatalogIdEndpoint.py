from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsEndpoint import ProcurementCatalogIdComponentsEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInfoEndpoint import ProcurementCatalogIdInfoEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdInventoryEndpoint import ProcurementCatalogIdInventoryEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdMinimumstockbywarehouseEndpoint import (
    ProcurementCatalogIdMinimumstockbywarehouseEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementCatalogIdPricingEndpoint import ProcurementCatalogIdPricingEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdQuantityonhandEndpoint import (
    ProcurementCatalogIdQuantityonhandEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import CatalogItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ProcurementCatalogIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[CatalogItem, ConnectWiseManageRequestParams],
    IPatchable[CatalogItem, ConnectWiseManageRequestParams],
    IPuttable[CatalogItem, ConnectWiseManageRequestParams],
    IPaginateable[CatalogItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, CatalogItem)
        IPatchable.__init__(self, CatalogItem)
        IPuttable.__init__(self, CatalogItem)
        IPaginateable.__init__(self, CatalogItem)

        self.components = self._register_child_endpoint(
            ProcurementCatalogIdComponentsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementCatalogIdInfoEndpoint(client, parent_endpoint=self))
        self.inventory = self._register_child_endpoint(
            ProcurementCatalogIdInventoryEndpoint(client, parent_endpoint=self)
        )
        self.minimum_stock_by_warehouse = self._register_child_endpoint(
            ProcurementCatalogIdMinimumstockbywarehouseEndpoint(client, parent_endpoint=self)
        )
        self.pricing = self._register_child_endpoint(ProcurementCatalogIdPricingEndpoint(client, parent_endpoint=self))
        self.quantity_on_hand = self._register_child_endpoint(
            ProcurementCatalogIdQuantityonhandEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CatalogItem]:
        """
        Performs a GET request against the /procurement/catalog/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogItem]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CatalogItem, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CatalogItem:
        """
        Performs a GET request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItem: The parsed response data.
        """
        return self._parse_one(CatalogItem, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> CatalogItem:
        """
        Performs a PATCH request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItem: The parsed response data.
        """
        return self._parse_one(CatalogItem, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CatalogItem:
        """
        Performs a PUT request against the /procurement/catalog/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItem: The parsed response data.
        """
        return self._parse_one(CatalogItem, super()._make_request("PUT", data=data, params=params).json())
