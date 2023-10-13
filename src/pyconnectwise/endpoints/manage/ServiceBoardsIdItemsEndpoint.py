from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsCountEndpoint import ServiceBoardsIdItemsCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdEndpoint import ServiceBoardsIdItemsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdItemsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardItem], ConnectWiseManageRequestParams],
    IPostable[BoardItem, ConnectWiseManageRequestParams],
    IPaginateable[BoardItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "items", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardItem])
        IPostable.__init__(self, BoardItem)
        IPaginateable.__init__(self, BoardItem)

        self.count = self._register_child_endpoint(ServiceBoardsIdItemsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdItemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdItemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdItemsIdEndpoint: The initialized ServiceBoardsIdItemsIdEndpoint object.
        """
        child = ServiceBoardsIdItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardItem]:
        """
        Performs a GET request against the /service/boards/{id}/items endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardItem]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), BoardItem, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[BoardItem]:
        """
        Performs a GET request against the /service/boards/{id}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardItem]: The parsed response data.
        """
        return self._parse_many(BoardItem, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardItem:
        """
        Performs a POST request against the /service/boards/{id}/items endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItem: The parsed response data.
        """
        return self._parse_one(BoardItem, super()._make_request("POST", data=data, params=params).json())
