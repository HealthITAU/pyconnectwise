from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsCountEndpoint import SystemLdapconfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsIdEndpoint import SystemLdapconfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsInfoEndpoint import SystemLdapconfigurationsInfoEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsTestlinkEndpoint import \
    SystemLdapconfigurationsTestlinkEndpoint
from pyconnectwise.models.manage import LdapConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemLdapconfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ldapConfigurations", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemLdapconfigurationsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemLdapconfigurationsInfoEndpoint(client, parent_endpoint=self))
        self.test_link = self._register_child_endpoint(
            SystemLdapconfigurationsTestlinkEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemLdapconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLdapconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLdapconfigurationsIdEndpoint: The initialized SystemLdapconfigurationsIdEndpoint object.
        """
        child = SystemLdapconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LdapConfiguration]:
        """
        Performs a GET request against the /system/ldapConfigurations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LdapConfiguration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LdapConfiguration, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LdapConfiguration]:
        """
        Performs a GET request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LdapConfiguration]: The parsed response data.
        """
        return self._parse_many(LdapConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LdapConfiguration:
        """
        Performs a POST request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LdapConfiguration: The parsed response data.
        """
        return self._parse_one(LdapConfiguration, super()._make_request("POST", data=data, params=params).json())
