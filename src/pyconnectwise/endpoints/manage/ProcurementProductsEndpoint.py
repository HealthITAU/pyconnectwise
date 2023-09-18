from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsCountEndpoint import ProcurementProductsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdEndpoint import ProcurementProductsIdEndpoint
from pyconnectwise.models.manage import ProductItem
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "products", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementProductsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementProductsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdEndpoint: The initialized ProcurementProductsIdEndpoint object.
        """
        child = ProcurementProductsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductItem]:
        """
        Performs a GET request against the /procurement/products endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductItem]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductItem, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductItem]:
        """
        Performs a GET request against the /procurement/products endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductItem]: The parsed response data.
        """
        return self._parse_many(ProductItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProductItem:
        """
        Performs a POST request against the /procurement/products endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductItem: The parsed response data.
        """
        return self._parse_one(ProductItem, super()._make_request("POST", data=data, params=params).json())
