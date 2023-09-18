from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSsousersCountEndpoint import SystemSsousersCountEndpoint
from pyconnectwise.endpoints.manage.SystemSsousersIdEndpoint import SystemSsousersIdEndpoint
from pyconnectwise.models.manage import SsoUser
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSsousersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ssoUsers", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemSsousersCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemSsousersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSsousersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSsousersIdEndpoint: The initialized SystemSsousersIdEndpoint object.
        """
        child = SystemSsousersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SsoUser]:
        """
        Performs a GET request against the /system/ssoUsers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SsoUser]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), SsoUser, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SsoUser]:
        """
        Performs a GET request against the /system/ssoUsers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SsoUser]: The parsed response data.
        """
        return self._parse_many(SsoUser, super()._make_request("GET", data=data, params=params).json())
