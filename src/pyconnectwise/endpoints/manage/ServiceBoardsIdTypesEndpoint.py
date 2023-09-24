from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesCountEndpoint import ServiceBoardsIdTypesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdTypesIdEndpoint import ServiceBoardsIdTypesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardType], ConnectWiseManageRequestParams],
    IPostable[BoardType, ConnectWiseManageRequestParams],
    IPaginateable[BoardType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(ServiceBoardsIdTypesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdTypesIdEndpoint: The initialized ServiceBoardsIdTypesIdEndpoint object.
        """
        child = ServiceBoardsIdTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardType]:
        """
        Performs a GET request against the /service/boards/{id}/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), BoardType, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[BoardType]:
        """
        Performs a GET request against the /service/boards/{id}/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardType]: The parsed response data.
        """
        return self._parse_many(BoardType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardType:
        """
        Performs a POST request against the /service/boards/{id}/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardType: The parsed response data.
        """
        return self._parse_one(BoardType, super()._make_request("POST", data=data, params=params).json())
