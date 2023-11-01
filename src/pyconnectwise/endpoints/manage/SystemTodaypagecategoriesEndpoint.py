from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemTodaypagecategoriesCountEndpoint import (
    SystemTodaypagecategoriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemTodaypagecategoriesIdEndpoint import (
    SystemTodaypagecategoriesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import TodayPageCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemTodaypagecategoriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TodayPageCategory], ConnectWiseManageRequestParams],
    IPostable[TodayPageCategory, ConnectWiseManageRequestParams],
    IPaginateable[TodayPageCategory, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "todayPageCategories", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TodayPageCategory])
        IPostable.__init__(self, TodayPageCategory)
        IPaginateable.__init__(self, TodayPageCategory)

        self.count = self._register_child_endpoint(
            SystemTodaypagecategoriesCountEndpoint(client, parent_endpoint=self)
        )

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
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TodayPageCategory,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TodayPageCategory]:
        """
        Performs a GET request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TodayPageCategory]: The parsed response data.
        """
        return self._parse_many(
            TodayPageCategory,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> TodayPageCategory:
        """
        Performs a POST request against the /system/todayPageCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TodayPageCategory: The parsed response data.
        """
        return self._parse_one(
            TodayPageCategory,
            super()._make_request("POST", data=data, params=params).json(),
        )
