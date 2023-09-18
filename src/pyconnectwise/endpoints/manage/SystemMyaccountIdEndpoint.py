from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdDelegationsEndpoint import SystemMyaccountIdDelegationsEndpoint
from pyconnectwise.endpoints.manage.SystemMyaccountIdSkillsEndpoint import SystemMyaccountIdSkillsEndpoint
from pyconnectwise.models.manage import MyAccount
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMyaccountIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.skills = self._register_child_endpoint(SystemMyaccountIdSkillsEndpoint(client, parent_endpoint=self))
        self.delegations = self._register_child_endpoint(
            SystemMyaccountIdDelegationsEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MyAccount]:
        """
        Performs a GET request against the /system/myAccount/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MyAccount]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), MyAccount, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccount:
        """
        Performs a GET request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccount: The parsed response data.
        """
        return self._parse_one(MyAccount, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccount:
        """
        Performs a PUT request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccount: The parsed response data.
        """
        return self._parse_one(MyAccount, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccount:
        """
        Performs a PATCH request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccount: The parsed response data.
        """
        return self._parse_one(MyAccount, super()._make_request("PATCH", data=data, params=params).json())
