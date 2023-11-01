from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousesCountEndpoint import (
    ProcurementWarehousesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementWarehousesIdEndpoint import (
    ProcurementWarehousesIdEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementWarehousesInfoEndpoint import (
    ProcurementWarehousesInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Warehouse
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementWarehousesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Warehouse], ConnectWiseManageRequestParams],
    IPostable[Warehouse, ConnectWiseManageRequestParams],
    IPaginateable[Warehouse, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "warehouses", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Warehouse])
        IPostable.__init__(self, Warehouse)
        IPaginateable.__init__(self, Warehouse)

        self.count = self._register_child_endpoint(
            ProcurementWarehousesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ProcurementWarehousesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementWarehousesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementWarehousesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementWarehousesIdEndpoint: The initialized ProcurementWarehousesIdEndpoint object.
        """
        child = ProcurementWarehousesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Warehouse]:
        """
        Performs a GET request against the /procurement/warehouses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Warehouse]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Warehouse,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Warehouse]:
        """
        Performs a GET request against the /procurement/warehouses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Warehouse]: The parsed response data.
        """
        return self._parse_many(
            Warehouse, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Warehouse:
        """
        Performs a POST request against the /procurement/warehouses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Warehouse: The parsed response data.
        """
        return self._parse_one(
            Warehouse, super()._make_request("POST", data=data, params=params).json()
        )
