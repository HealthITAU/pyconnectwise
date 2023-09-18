from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorloginsCountEndpoint import SystemIntegratorloginsCountEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorloginsIdEndpoint import SystemIntegratorloginsIdEndpoint
from pyconnectwise.models.manage import IntegratorLogin
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemIntegratorloginsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "integratorlogins", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemIntegratorloginsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemIntegratorloginsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemIntegratorloginsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemIntegratorloginsIdEndpoint: The initialized SystemIntegratorloginsIdEndpoint object.
        """
        child = SystemIntegratorloginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[IntegratorLogin]:
        """
        Performs a GET request against the /system/integratorlogins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IntegratorLogin]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), IntegratorLogin, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[IntegratorLogin]:
        """
        Performs a GET request against the /system/integratorlogins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[IntegratorLogin]: The parsed response data.
        """
        return self._parse_many(IntegratorLogin, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> IntegratorLogin:
        """
        Performs a POST request against the /system/integratorlogins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IntegratorLogin: The parsed response data.
        """
        return self._parse_one(IntegratorLogin, super()._make_request("POST", data=data, params=params).json())
