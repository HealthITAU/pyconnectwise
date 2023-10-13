from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdNotificationsCountEndpoint import \
    ServiceBoardsIdStatusesIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdNotificationsIdEndpoint import \
    ServiceBoardsIdStatusesIdNotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardStatusNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdStatusesIdNotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardStatusNotification], ConnectWiseManageRequestParams],
    IPostable[BoardStatusNotification, ConnectWiseManageRequestParams],
    IPaginateable[BoardStatusNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notifications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardStatusNotification])
        IPostable.__init__(self, BoardStatusNotification)
        IPaginateable.__init__(self, BoardStatusNotification)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdStatusesIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdStatusesIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdStatusesIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdStatusesIdNotificationsIdEndpoint: The initialized ServiceBoardsIdStatusesIdNotificationsIdEndpoint object.
        """
        child = ServiceBoardsIdStatusesIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardStatusNotification]:
        """
        Performs a GET request against the /service/boards/{id}/statuses/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardStatusNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardStatusNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardStatusNotification]:
        """
        Performs a GET request against the /service/boards/{id}/statuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardStatusNotification]: The parsed response data.
        """
        return self._parse_many(BoardStatusNotification, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> BoardStatusNotification:
        """
        Performs a POST request against the /service/boards/{id}/statuses/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatusNotification: The parsed response data.
        """
        return self._parse_one(BoardStatusNotification, super()._make_request("POST", data=data, params=params).json())
