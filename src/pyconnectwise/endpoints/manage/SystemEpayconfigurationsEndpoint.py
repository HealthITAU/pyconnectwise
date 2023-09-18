from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEpayconfigurationsCountEndpoint import SystemEpayconfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemEpayconfigurationsIdEndpoint import SystemEpayconfigurationsIdEndpoint
from pyconnectwise.models.manage import EPayConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemEpayconfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ePayConfigurations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemEpayconfigurationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemEpayconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEpayconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEpayconfigurationsIdEndpoint: The initialized SystemEpayconfigurationsIdEndpoint object.
        """
        child = SystemEpayconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[EPayConfiguration]:
        """
        Performs a GET request against the /system/ePayConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EPayConfiguration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), EPayConfiguration, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[EPayConfiguration]:
        """
        Performs a GET request against the /system/ePayConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EPayConfiguration]: The parsed response data.
        """
        return self._parse_many(EPayConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> EPayConfiguration:
        """
        Performs a POST request against the /system/ePayConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EPayConfiguration: The parsed response data.
        """
        return self._parse_one(EPayConfiguration, super()._make_request("POST", data=data, params=params).json())
