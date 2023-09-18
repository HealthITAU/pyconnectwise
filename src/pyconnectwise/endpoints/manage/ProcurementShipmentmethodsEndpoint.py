from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsCountEndpoint import \
    ProcurementShipmentmethodsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsIdEndpoint import ProcurementShipmentmethodsIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsInfoEndpoint import ProcurementShipmentmethodsInfoEndpoint
from pyconnectwise.models.manage import ShipmentMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementShipmentmethodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "shipmentmethods", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementShipmentmethodsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(ProcurementShipmentmethodsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementShipmentmethodsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementShipmentmethodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementShipmentmethodsIdEndpoint: The initialized ProcurementShipmentmethodsIdEndpoint object.
        """
        child = ProcurementShipmentmethodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ShipmentMethod]:
        """
        Performs a GET request against the /procurement/shipmentmethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ShipmentMethod]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ShipmentMethod, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ShipmentMethod]:
        """
        Performs a GET request against the /procurement/shipmentmethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ShipmentMethod]: The parsed response data.
        """
        return self._parse_many(ShipmentMethod, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ShipmentMethod:
        """
        Performs a POST request against the /procurement/shipmentmethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ShipmentMethod: The parsed response data.
        """
        return self._parse_one(ShipmentMethod, super()._make_request("POST", data=data, params=params).json())
