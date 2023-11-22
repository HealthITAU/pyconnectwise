from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsCountEndpoint import SystemLdapconfigurationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsIdEndpoint import SystemLdapconfigurationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsInfoEndpoint import SystemLdapconfigurationsInfoEndpoint
from pyconnectwise.endpoints.manage.SystemLdapconfigurationsTestlinkEndpoint import (
    SystemLdapconfigurationsTestlinkEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import LdapConfiguration
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemLdapconfigurationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LdapConfiguration], ConnectWiseManageRequestParams],
    IPostable[LdapConfiguration, ConnectWiseManageRequestParams],
    IPaginateable[LdapConfiguration, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "ldapConfigurations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LdapConfiguration])
        IPostable.__init__(self, LdapConfiguration)
        IPaginateable.__init__(self, LdapConfiguration)

        self.count = self._register_child_endpoint(SystemLdapconfigurationsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemLdapconfigurationsInfoEndpoint(client, parent_endpoint=self))
        self.test_link = self._register_child_endpoint(
            SystemLdapconfigurationsTestlinkEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> SystemLdapconfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLdapconfigurationsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemLdapconfigurationsIdEndpoint: The initialized SystemLdapconfigurationsIdEndpoint object.
        """
        child = SystemLdapconfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LdapConfiguration, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[LdapConfiguration]:
        """
        Performs a GET request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LdapConfiguration]: The parsed response data.
        """
        return self._parse_many(LdapConfiguration, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> LdapConfiguration:
        """
        Performs a POST request against the /system/ldapConfigurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LdapConfiguration: The parsed response data.
        """
        return self._parse_one(LdapConfiguration, super()._make_request("POST", data=data, params=params).json())
