from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsCountEndpoint import SystemSettingsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsIdEndpoint import SystemSettingsIdEndpoint
from pyconnectwise.models.manage import SystemSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemSettingsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSettingsIdEndpoint: The initialized SystemSettingsIdEndpoint object.
        """
        child = SystemSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[SystemSetting]:
        """
        Performs a GET request against the /system/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SystemSetting]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SystemSetting, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SystemSetting]:
        """
        Performs a GET request against the /system/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SystemSetting]: The parsed response data.
        """
        return self._parse_many(SystemSetting, super()._make_request("GET", data=data, params=params).json())
