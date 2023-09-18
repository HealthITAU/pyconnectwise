from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliverymethodsCountEndpoint import FinanceDeliverymethodsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceDeliverymethodsIdEndpoint import FinanceDeliverymethodsIdEndpoint
from pyconnectwise.models.manage import DeliveryMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceDeliverymethodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "deliveryMethods", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(FinanceDeliverymethodsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceDeliverymethodsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceDeliverymethodsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceDeliverymethodsIdEndpoint: The initialized FinanceDeliverymethodsIdEndpoint object.
        """
        child = FinanceDeliverymethodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[DeliveryMethod]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DeliveryMethod]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DeliveryMethod, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DeliveryMethod]:
        """
        Performs a GET request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DeliveryMethod]: The parsed response data.
        """
        return self._parse_many(DeliveryMethod, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> DeliveryMethod:
        """
        Performs a POST request against the /finance/deliveryMethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DeliveryMethod: The parsed response data.
        """
        return self._parse_one(DeliveryMethod, super()._make_request("POST", data=data, params=params).json())
