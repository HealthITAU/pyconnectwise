from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdInfoEndpoint import (
    ServiceBoardsIdStatusesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdNotificationsEndpoint import (
    ServiceBoardsIdStatusesIdNotificationsEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdUsagesEndpoint import (
    ServiceBoardsIdStatusesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import BoardStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceBoardsIdStatusesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[BoardStatus, ConnectWiseManageRequestParams],
    IPuttable[BoardStatus, ConnectWiseManageRequestParams],
    IPatchable[BoardStatus, ConnectWiseManageRequestParams],
    IPaginateable[BoardStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, BoardStatus)
        IPuttable.__init__(self, BoardStatus)
        IPatchable.__init__(self, BoardStatus)
        IPaginateable.__init__(self, BoardStatus)

        self.usages = self._register_child_endpoint(
            ServiceBoardsIdStatusesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.notifications = self._register_child_endpoint(
            ServiceBoardsIdStatusesIdNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ServiceBoardsIdStatusesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardStatus]:
        """
        Performs a GET request against the /service/boards/{id}/statuses/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardStatus]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardStatus,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardStatus:
        """
        Performs a GET request against the /service/boards/{id}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatus: The parsed response data.
        """
        return self._parse_one(
            BoardStatus, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/boards/{id}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardStatus:
        """
        Performs a PUT request against the /service/boards/{id}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatus: The parsed response data.
        """
        return self._parse_one(
            BoardStatus, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardStatus:
        """
        Performs a PATCH request against the /service/boards/{id}/statuses/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatus: The parsed response data.
        """
        return self._parse_one(
            BoardStatus, super()._make_request("PATCH", data=data, params=params).json()
        )
