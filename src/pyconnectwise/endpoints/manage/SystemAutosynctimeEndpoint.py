from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAutosynctimeCountEndpoint import (
    SystemAutosynctimeCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemAutosynctimeIdEndpoint import (
    SystemAutosynctimeIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AutoSyncTime
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemAutosynctimeEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutoSyncTime], ConnectWiseManageRequestParams],
    IPostable[AutoSyncTime, ConnectWiseManageRequestParams],
    IPaginateable[AutoSyncTime, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "autoSyncTime", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutoSyncTime])
        IPostable.__init__(self, AutoSyncTime)
        IPaginateable.__init__(self, AutoSyncTime)

        self.count = self._register_child_endpoint(
            SystemAutosynctimeCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemAutosynctimeIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemAutosynctimeIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemAutosynctimeIdEndpoint: The initialized SystemAutosynctimeIdEndpoint object.
        """
        child = SystemAutosynctimeIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AutoSyncTime]:
        """
        Performs a GET request against the /system/autoSyncTime endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutoSyncTime]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutoSyncTime,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AutoSyncTime]:
        """
        Performs a GET request against the /system/autoSyncTime endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutoSyncTime]: The parsed response data.
        """
        return self._parse_many(
            AutoSyncTime, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AutoSyncTime:
        """
        Performs a POST request against the /system/autoSyncTime endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutoSyncTime: The parsed response data.
        """
        return self._parse_one(
            AutoSyncTime, super()._make_request("POST", data=data, params=params).json()
        )
