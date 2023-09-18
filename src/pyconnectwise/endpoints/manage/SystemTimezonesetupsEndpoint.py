from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemTimezonesetupsCountEndpoint import SystemTimezonesetupsCountEndpoint
from pyconnectwise.endpoints.manage.SystemTimezonesetupsIdEndpoint import SystemTimezonesetupsIdEndpoint
from pyconnectwise.endpoints.manage.SystemTimezonesetupsInfoEndpoint import SystemTimezonesetupsInfoEndpoint
from pyconnectwise.models.manage import TimeZoneSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemTimezonesetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeZoneSetups", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemTimezonesetupsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemTimezonesetupsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemTimezonesetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemTimezonesetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemTimezonesetupsIdEndpoint: The initialized SystemTimezonesetupsIdEndpoint object.
        """
        child = SystemTimezonesetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TimeZoneSetup]:
        """
        Performs a GET request against the /system/timeZoneSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeZoneSetup]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TimeZoneSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TimeZoneSetup]:
        """
        Performs a GET request against the /system/timeZoneSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeZoneSetup]: The parsed response data.
        """
        return self._parse_many(TimeZoneSetup, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TimeZoneSetup:
        """
        Performs a POST request against the /system/timeZoneSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TimeZoneSetup: The parsed response data.
        """
        return self._parse_one(TimeZoneSetup, super()._make_request("POST", data=data, params=params).json())
