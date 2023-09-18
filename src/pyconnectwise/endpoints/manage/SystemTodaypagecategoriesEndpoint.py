from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemTodaypagecategoriesCountEndpoint import SystemTodaypagecategoriesCountEndpoint
from pyconnectwise.endpoints.manage.SystemTodaypagecategoriesIdEndpoint import SystemTodaypagecategoriesIdEndpoint
from pyconnectwise.models.manage import TodayPageCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemTodaypagecategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "todayPageCategories", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemTodaypagecategoriesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemTodaypagecategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemTodaypagecategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemTodaypagecategoriesIdEndpoint: The initialized SystemTodaypagecategoriesIdEndpoint object.
        """
        child = SystemTodaypagecategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[TodayPageCategory]:
        """
        Performs a GET request against the /system/todayPageCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TodayPageCategory]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), TodayPageCategory, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TodayPageCategory]:
        """
        Performs a GET request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TodayPageCategory]: The parsed response data.
        """
        return self._parse_many(TodayPageCategory, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TodayPageCategory:
        """
        Performs a POST request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TodayPageCategory: The parsed response data.
        """
        return self._parse_one(TodayPageCategory, super()._make_request("POST", data=data, params=params).json())
