from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogCountEndpoint import ProcurementCatalogCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogIdEndpoint import ProcurementCatalogIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogInfoEndpoint import ProcurementCatalogInfoEndpoint
from pyconnectwise.models.manage import CatalogItem
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementCatalogEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "catalog", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ProcurementCatalogCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ProcurementCatalogInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ProcurementCatalogIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementCatalogIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementCatalogIdEndpoint: The initialized ProcurementCatalogIdEndpoint object.
        """
        child = ProcurementCatalogIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CatalogItem]:
        """
        Performs a GET request against the /procurement/catalog endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CatalogItem]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CatalogItem, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CatalogItem]:
        """
        Performs a GET request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CatalogItem]: The parsed response data.
        """
        return self._parse_many(CatalogItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CatalogItem:
        """
        Performs a POST request against the /procurement/catalog endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CatalogItem: The parsed response data.
        """
        return self._parse_one(CatalogItem, super()._make_request("POST", data=data, params=params).json())
