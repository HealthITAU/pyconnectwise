from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsCountEndpoint import \
    ProcurementCatalogIdComponentsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdComponentsIdEndpoint import \
    ProcurementCatalogIdComponentsIdEndpoint
from pyconnectwise.models.manage import CatalogComponent
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementCatalogIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementCatalogIdComponentsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementCatalogIdComponentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdComponentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdComponentsIdEndpoint: The initialized ProcurementCatalogIdComponentsIdEndpoint object.
        """
        child = ProcurementCatalogIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CatalogComponent]:
        """
        Performs a GET request against the /procurement/catalog/{id}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogComponent]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CatalogComponent, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CatalogComponent]:
        """
        Performs a GET request against the /procurement/catalog/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogComponent]: The parsed response data.
        """
        return self._parse_many(CatalogComponent, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogComponent:
        """
        Performs a POST request against the /procurement/catalog/{id}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogComponent: The parsed response data.
        """
        return self._parse_one(CatalogComponent, super()._make_request("POST", data=data, params=params).json())
