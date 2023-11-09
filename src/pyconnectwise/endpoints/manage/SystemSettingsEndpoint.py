from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsCountEndpoint import SystemSettingsCountEndpoint
from pyconnectwise.endpoints.manage.SystemSettingsIdEndpoint import SystemSettingsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import SystemSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemSettingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SystemSetting], ConnectWiseManageRequestParams],
    IPaginateable[SystemSetting, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "settings", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SystemSetting])
        IPaginateable.__init__(self, SystemSetting)

        self.count = self._register_child_endpoint(SystemSettingsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSettingsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemSettingsIdEndpoint: The initialized SystemSettingsIdEndpoint object.
        """
        child = SystemSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), SystemSetting, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[SystemSetting]:
        """
        Performs a GET request against the /system/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SystemSetting]: The parsed response data.
        """
        return self._parse_many(SystemSetting, super()._make_request("GET", data=data, params=params).json())
