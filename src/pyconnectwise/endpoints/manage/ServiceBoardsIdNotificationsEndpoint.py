from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdNotificationsCountEndpoint import \
    ServiceBoardsIdNotificationsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdNotificationsIdEndpoint import ServiceBoardsIdNotificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardNotification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdNotificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardNotification], ConnectWiseManageRequestParams],
    IPostable[BoardNotification, ConnectWiseManageRequestParams],
    IPaginateable[BoardNotification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notifications", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardNotification])
        IPostable.__init__(self, BoardNotification)
        IPaginateable.__init__(self, BoardNotification)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdNotificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdNotificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdNotificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdNotificationsIdEndpoint: The initialized ServiceBoardsIdNotificationsIdEndpoint object.
        """
        child = ServiceBoardsIdNotificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardNotification]:
        """
        Performs a GET request against the /service/boards/{id}/notifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardNotification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardNotification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardNotification]:
        """
        Performs a GET request against the /service/boards/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardNotification]: The parsed response data.
        """
        return self._parse_many(BoardNotification, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardNotification:
        """
        Performs a POST request against the /service/boards/{id}/notifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardNotification: The parsed response data.
        """
        return self._parse_one(BoardNotification, super()._make_request("POST", data=data, params=params).json())
