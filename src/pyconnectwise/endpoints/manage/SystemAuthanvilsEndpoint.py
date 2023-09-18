from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAuthanvilsCountEndpoint import SystemAuthanvilsCountEndpoint
from pyconnectwise.endpoints.manage.SystemAuthanvilsIdEndpoint import SystemAuthanvilsIdEndpoint
from pyconnectwise.endpoints.manage.SystemAuthanvilsTestconnectionEndpoint import SystemAuthanvilsTestconnectionEndpoint
from pyconnectwise.models.manage import AuthAnvil
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemAuthanvilsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "authAnvils", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemAuthanvilsCountEndpoint(client, parent_endpoint=self))
        self.test_connection = self._register_child_endpoint(
            SystemAuthanvilsTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemAuthanvilsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemAuthanvilsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemAuthanvilsIdEndpoint: The initialized SystemAuthanvilsIdEndpoint object.
        """
        child = SystemAuthanvilsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AuthAnvil]:
        """
        Performs a GET request against the /system/authAnvils endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AuthAnvil]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), AuthAnvil, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AuthAnvil]:
        """
        Performs a GET request against the /system/authAnvils endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AuthAnvil]: The parsed response data.
        """
        return self._parse_many(AuthAnvil, super()._make_request("GET", data=data, params=params).json())
