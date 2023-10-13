from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesCountEndpoint import ServiceBoardsIdSubtypesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesIdEndpoint import ServiceBoardsIdSubtypesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesInfoEndpoint import ServiceBoardsIdSubtypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdSubtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardSubType], ConnectWiseManageRequestParams],
    IPostable[BoardSubType, ConnectWiseManageRequestParams],
    IPaginateable[BoardSubType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "subtypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardSubType])
        IPostable.__init__(self, BoardSubType)
        IPaginateable.__init__(self, BoardSubType)

        self.count = self._register_child_endpoint(ServiceBoardsIdSubtypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ServiceBoardsIdSubtypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceBoardsIdSubtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdSubtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdSubtypesIdEndpoint: The initialized ServiceBoardsIdSubtypesIdEndpoint object.
        """
        child = ServiceBoardsIdSubtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardSubType]:
        """
        Performs a GET request against the /service/boards/{id}/subtypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardSubType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardSubType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[BoardSubType]:
        """
        Performs a GET request against the /service/boards/{id}/subtypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardSubType]: The parsed response data.
        """
        return self._parse_many(BoardSubType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> BoardSubType:
        """
        Performs a POST request against the /service/boards/{id}/subtypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardSubType: The parsed response data.
        """
        return self._parse_one(BoardSubType, super()._make_request("POST", data=data, params=params).json())
