from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdSettingsCountEndpoint import \
    SystemSecurityrolesIdSettingsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSecurityrolesIdSettingsIdEndpoint import \
    SystemSecurityrolesIdSettingsIdEndpoint
from pyconnectwise.models.manage import SecurityRoleSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSecurityrolesIdSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemSecurityrolesIdSettingsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemSecurityrolesIdSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSecurityrolesIdSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSecurityrolesIdSettingsIdEndpoint: The initialized SystemSecurityrolesIdSettingsIdEndpoint object.
        """
        child = SystemSecurityrolesIdSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SecurityRoleSetting]:
        """
        Performs a GET request against the /system/securityRoles/{id}/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SecurityRoleSetting]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SecurityRoleSetting, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SecurityRoleSetting]:
        """
        Performs a GET request against the /system/securityRoles/{id}/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SecurityRoleSetting]: The parsed response data.
        """
        return self._parse_many(SecurityRoleSetting, super()._make_request("GET", data=data, params=params).json())
