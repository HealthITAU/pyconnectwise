from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdExcludedmembersCountEndpoint import \
    ServiceBoardsIdExcludedmembersCountEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdExcludedmembersIdEndpoint import \
    ServiceBoardsIdExcludedmembersIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BoardExcludedMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceBoardsIdExcludedmembersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardExcludedMember], ConnectWiseManageRequestParams],
    IPostable[BoardExcludedMember, ConnectWiseManageRequestParams],
    IPaginateable[BoardExcludedMember, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "excludedMembers", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardExcludedMember])
        IPostable.__init__(self, BoardExcludedMember)
        IPaginateable.__init__(self, BoardExcludedMember)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdExcludedmembersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceBoardsIdExcludedmembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdExcludedmembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdExcludedmembersIdEndpoint: The initialized ServiceBoardsIdExcludedmembersIdEndpoint object.
        """
        child = ServiceBoardsIdExcludedmembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardExcludedMember]:
        """
        Performs a GET request against the /service/boards/{id}/excludedMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardExcludedMember]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardExcludedMember, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardExcludedMember]:
        """
        Performs a GET request against the /service/boards/{id}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardExcludedMember]: The parsed response data.
        """
        return self._parse_many(BoardExcludedMember, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> BoardExcludedMember:
        """
        Performs a POST request against the /service/boards/{id}/excludedMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardExcludedMember: The parsed response data.
        """
        return self._parse_one(BoardExcludedMember, super()._make_request("POST", data=data, params=params).json())
