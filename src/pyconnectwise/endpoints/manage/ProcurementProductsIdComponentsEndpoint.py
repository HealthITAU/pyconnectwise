from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdComponentsCountEndpoint import \
    ProcurementProductsIdComponentsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsIdComponentsIdEndpoint import \
    ProcurementProductsIdComponentsIdEndpoint
from pyconnectwise.models.manage import ProductComponent
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementProductsIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementProductsIdComponentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementProductsIdComponentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementProductsIdComponentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementProductsIdComponentsIdEndpoint: The initialized ProcurementProductsIdComponentsIdEndpoint object.
        """
        child = ProcurementProductsIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProductComponent]:
        """
        Performs a GET request against the /procurement/products/{id}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductComponent]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductComponent, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductComponent]:
        """
        Performs a GET request against the /procurement/products/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponent]: The parsed response data.
        """
        return self._parse_many(ProductComponent, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductComponent]:
        """
        Performs a POST request against the /procurement/products/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponent]: The parsed response data.
        """
        return self._parse_many(ProductComponent, super()._make_request("POST", data=data, params=params).json())
