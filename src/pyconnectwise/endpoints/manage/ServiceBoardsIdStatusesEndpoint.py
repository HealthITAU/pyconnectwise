from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesCountEndpoint import ServiceBoardsIdStatusesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesIdEndpoint import ServiceBoardsIdStatusesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdStatusesInfoEndpoint import ServiceBoardsIdStatusesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardStatus
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdStatusesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardStatus], ConnectWiseManageRequestParams],
    IPostable[BoardStatus, ConnectWiseManageRequestParams],
    IPaginateable[BoardStatus, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "statuses", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardStatus])
        IPostable.__init__(self, BoardStatus)
        IPaginateable.__init__(self, BoardStatus)

        self.count = self._register_child_endpoint(ServiceBoardsIdStatusesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceBoardsIdStatusesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdStatusesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdStatusesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdStatusesIdEndpoint: The initialized ServiceBoardsIdStatusesIdEndpoint object.
        """
        child = ServiceBoardsIdStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardStatus]:
        """
        Performs a GET request against the /service/boards/{id}/statuses endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params), BoardStatus, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[BoardStatus]:
        """
        Performs a GET request against the /service/boards/{id}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardStatus]: The parsed response data.
        """
        return self._parse_many(BoardStatus, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardStatus:
        """
        Performs a POST request against the /service/boards/{id}/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardStatus: The parsed response data.
        """
        return self._parse_one(BoardStatus, super()._make_request("POST", data=data, params=params).json())
