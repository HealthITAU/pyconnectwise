from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemQuotelinksetupCountEndpoint import SystemQuotelinksetupCountEndpoint
from pyconnectwise.endpoints.manage.SystemQuotelinksetupIdEndpoint import SystemQuotelinksetupIdEndpoint
from pyconnectwise.endpoints.manage.SystemQuotelinksetupTestconnectionEndpoint import \
    SystemQuotelinksetupTestconnectionEndpoint
from pyconnectwise.models.manage import QuoteLink
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemQuotelinksetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "quoteLinkSetup", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemQuotelinksetupCountEndpoint(client, parent_endpoint=self))
        self.test_connection = self._register_child_endpoint(
            SystemQuotelinksetupTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemQuotelinksetupIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemQuotelinksetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemQuotelinksetupIdEndpoint: The initialized SystemQuotelinksetupIdEndpoint object.
        """
        child = SystemQuotelinksetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[QuoteLink]:
        """
        Performs a GET request against the /system/quoteLinkSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[QuoteLink]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), QuoteLink, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[QuoteLink]:
        """
        Performs a GET request against the /system/quoteLinkSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[QuoteLink]: The parsed response data.
        """
        return self._parse_many(QuoteLink, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> QuoteLink:
        """
        Performs a POST request against the /system/quoteLinkSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            QuoteLink: The parsed response data.
        """
        return self._parse_one(QuoteLink, super()._make_request("POST", data=data, params=params).json())
