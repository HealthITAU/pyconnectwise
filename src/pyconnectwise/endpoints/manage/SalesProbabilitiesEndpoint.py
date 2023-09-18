from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesProbabilitiesCountEndpoint import SalesProbabilitiesCountEndpoint
from pyconnectwise.endpoints.manage.SalesProbabilitiesIdEndpoint import SalesProbabilitiesIdEndpoint
from pyconnectwise.endpoints.manage.SalesProbabilitiesInfoEndpoint import SalesProbabilitiesInfoEndpoint
from pyconnectwise.models.manage import SalesProbability
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesProbabilitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "probabilities", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesProbabilitiesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SalesProbabilitiesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SalesProbabilitiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesProbabilitiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesProbabilitiesIdEndpoint: The initialized SalesProbabilitiesIdEndpoint object.
        """
        child = SalesProbabilitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SalesProbability]:
        """
        Performs a GET request against the /sales/probabilities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesProbability]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SalesProbability, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SalesProbability]:
        """
        Performs a GET request against the /sales/probabilities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesProbability]: The parsed response data.
        """
        return self._parse_many(SalesProbability, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SalesProbability:
        """
        Performs a POST request against the /sales/probabilities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesProbability: The parsed response data.
        """
        return self._parse_one(SalesProbability, super()._make_request("POST", data=data, params=params).json())
