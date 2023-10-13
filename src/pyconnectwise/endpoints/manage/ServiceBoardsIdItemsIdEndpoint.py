from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdAssociationsEndpoint import \
    ServiceBoardsIdItemsIdAssociationsEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdItemsIdUsagesEndpoint import ServiceBoardsIdItemsIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardItem
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdItemsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[BoardItem, ConnectWiseManageRequestParams],
    IPuttable[BoardItem, ConnectWiseManageRequestParams],
    IPatchable[BoardItem, ConnectWiseManageRequestParams],
    IPaginateable[BoardItem, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, BoardItem)
        IPuttable.__init__(self, BoardItem)
        IPatchable.__init__(self, BoardItem)
        IPaginateable.__init__(self, BoardItem)

        self.associations = self._register_child_endpoint(
            ServiceBoardsIdItemsIdAssociationsEndpoint(client, parent_endpoint=self)
        )
        self.usages = self._register_child_endpoint(ServiceBoardsIdItemsIdUsagesEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardItem]:
        """
        Performs a GET request against the /service/boards/{id}/items/{id} endpoint and returns an initialized PaginatedResponse object.

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

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardItem:
        """
        Performs a GET request against the /service/boards/{id}/items/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItem: The parsed response data.
        """
        return self._parse_one(BoardItem, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /service/boards/{id}/items/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardItem:
        """
        Performs a PUT request against the /service/boards/{id}/items/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItem: The parsed response data.
        """
        return self._parse_one(BoardItem, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> BoardItem:
        """
        Performs a PATCH request against the /service/boards/{id}/items/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardItem: The parsed response data.
        """
        return self._parse_one(BoardItem, super()._make_request("PATCH", data=data, params=params).json())
