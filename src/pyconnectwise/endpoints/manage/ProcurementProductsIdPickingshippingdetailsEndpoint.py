from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingshippingdetailsCountEndpoint import \
    ProcurementProductsIdPickingshippingdetailsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdPickingshippingdetailsIdEndpoint import \
    ProcurementProductsIdPickingshippingdetailsIdEndpoint
from pyconnectwise.models.manage import ProductPickingShippingDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementProductsIdPickingshippingdetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "pickingShippingDetails", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementProductsIdPickingshippingdetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementProductsIdPickingshippingdetailsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdPickingshippingdetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdPickingshippingdetailsIdEndpoint: The initialized ProcurementProductsIdPickingshippingdetailsIdEndpoint object.
        """
        child = ProcurementProductsIdPickingshippingdetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProductPickingShippingDetail]:
        """
        Performs a GET request against the /procurement/products/{id}/pickingShippingDetails endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductPickingShippingDetail]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductPickingShippingDetail, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductPickingShippingDetail]:
        """
        Performs a GET request against the /procurement/products/{id}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetail]: The parsed response data.
        """
        return self._parse_many(
            ProductPickingShippingDetail, super()._make_request("GET", data=data, params=params).json()
        )

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductPickingShippingDetail]:
        """
        Performs a POST request against the /procurement/products/{id}/pickingShippingDetails endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductPickingShippingDetail]: The parsed response data.
        """
        return self._parse_many(
            ProductPickingShippingDetail, super()._make_request("POST", data=data, params=params).json()
        )
