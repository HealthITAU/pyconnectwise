from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSetupscreensCountEndpoint import SystemSetupscreensCountEndpoint
from pyconnectwise.endpoints.manage.SystemSetupscreensIdEndpoint import SystemSetupscreensIdEndpoint
from pyconnectwise.models.manage import SetupScreen
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemSetupscreensEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "setupScreens", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemSetupscreensCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemSetupscreensIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemSetupscreensIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemSetupscreensIdEndpoint: The initialized SystemSetupscreensIdEndpoint object.
        """
        child = SystemSetupscreensIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SetupScreen]:
        """
        Performs a GET request against the /system/setupScreens endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SetupScreen]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), SetupScreen, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SetupScreen]:
        """
        Performs a GET request against the /system/setupScreens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SetupScreen]: The parsed response data.
        """
        return self._parse_many(SetupScreen, super()._make_request("GET", data=data, params=params).json())
