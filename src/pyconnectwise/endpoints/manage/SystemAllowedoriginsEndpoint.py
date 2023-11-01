from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemAllowedoriginsCountEndpoint import (
    SystemAllowedoriginsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemAllowedoriginsIdEndpoint import (
    SystemAllowedoriginsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import AllowedOrigin
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemAllowedoriginsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AllowedOrigin], ConnectWiseManageRequestParams],
    IPostable[AllowedOrigin, ConnectWiseManageRequestParams],
    IPaginateable[AllowedOrigin, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "allowedorigins", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AllowedOrigin])
        IPostable.__init__(self, AllowedOrigin)
        IPaginateable.__init__(self, AllowedOrigin)

        self.count = self._register_child_endpoint(
            SystemAllowedoriginsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemAllowedoriginsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemAllowedoriginsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemAllowedoriginsIdEndpoint: The initialized SystemAllowedoriginsIdEndpoint object.
        """
        child = SystemAllowedoriginsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[AllowedOrigin]:
        """
        Performs a GET request against the /system/allowedorigins endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AllowedOrigin]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AllowedOrigin,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[AllowedOrigin]:
        """
        Performs a GET request against the /system/allowedorigins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AllowedOrigin]: The parsed response data.
        """
        return self._parse_many(
            AllowedOrigin, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> AllowedOrigin:
        """
        Performs a POST request against the /system/allowedorigins endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AllowedOrigin: The parsed response data.
        """
        return self._parse_one(
            AllowedOrigin,
            super()._make_request("POST", data=data, params=params).json(),
        )
