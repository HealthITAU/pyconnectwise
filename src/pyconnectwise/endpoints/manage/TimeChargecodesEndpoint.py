from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesCountEndpoint import TimeChargecodesCountEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesIdEndpoint import TimeChargecodesIdEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesInfoEndpoint import TimeChargecodesInfoEndpoint
from pyconnectwise.models.manage import ChargeCode
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeChargecodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "chargeCodes", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(TimeChargecodesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(TimeChargecodesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> TimeChargecodesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeChargecodesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeChargecodesIdEndpoint: The initialized TimeChargecodesIdEndpoint object.
        """
        child = TimeChargecodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ChargeCode]:
        """
        Performs a GET request against the /time/chargeCodes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ChargeCode]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), ChargeCode, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ChargeCode]:
        """
        Performs a GET request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ChargeCode]: The parsed response data.
        """
        return self._parse_many(ChargeCode, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ChargeCode:
        """
        Performs a POST request against the /time/chargeCodes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ChargeCode: The parsed response data.
        """
        return self._parse_one(ChargeCode, super()._make_request("POST", data=data, params=params).json())
