from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementDirectionalsyncsCountEndpoint import \
    ProcurementDirectionalsyncsCountEndpoint
from pyconnectwise.endpoints.manage.ProcurementDirectionalsyncsIdEndpoint import ProcurementDirectionalsyncsIdEndpoint
from pyconnectwise.models.manage import DirectionalSync
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementDirectionalsyncsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "directionalSyncs", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ProcurementDirectionalsyncsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementDirectionalsyncsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementDirectionalsyncsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementDirectionalsyncsIdEndpoint: The initialized ProcurementDirectionalsyncsIdEndpoint object.
        """
        child = ProcurementDirectionalsyncsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[DirectionalSync]:
        """
        Performs a GET request against the /procurement/directionalSyncs endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DirectionalSync]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DirectionalSync, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DirectionalSync]:
        """
        Performs a GET request against the /procurement/directionalSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DirectionalSync]: The parsed response data.
        """
        return self._parse_many(DirectionalSync, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DirectionalSync:
        """
        Performs a POST request against the /procurement/directionalSyncs endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DirectionalSync: The parsed response data.
        """
        return self._parse_one(DirectionalSync, super()._make_request("POST", data=data, params=params).json())
