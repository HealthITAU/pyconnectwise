from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoassignresourcesCountEndpoint import (
    ServiceBoardsIdAutoassignresourcesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoassignresourcesIdEndpoint import (
    ServiceBoardsIdAutoassignresourcesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import BoardAutoAssignResource
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceBoardsIdAutoassignresourcesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardAutoAssignResource], ConnectWiseManageRequestParams],
    IPostable[BoardAutoAssignResource, ConnectWiseManageRequestParams],
    IPaginateable[BoardAutoAssignResource, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "autoAssignResources", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BoardAutoAssignResource])
        IPostable.__init__(self, BoardAutoAssignResource)
        IPaginateable.__init__(self, BoardAutoAssignResource)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdAutoassignresourcesCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> ServiceBoardsIdAutoassignresourcesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdAutoassignresourcesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdAutoassignresourcesIdEndpoint: The initialized ServiceBoardsIdAutoassignresourcesIdEndpoint object.
        """
        child = ServiceBoardsIdAutoassignresourcesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardAutoAssignResource]:
        """
        Performs a GET request against the /service/boards/{id}/autoAssignResources endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardAutoAssignResource]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardAutoAssignResource,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BoardAutoAssignResource]:
        """
        Performs a GET request against the /service/boards/{id}/autoAssignResources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardAutoAssignResource]: The parsed response data.
        """
        return self._parse_many(
            BoardAutoAssignResource,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardAutoAssignResource:
        """
        Performs a POST request against the /service/boards/{id}/autoAssignResources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardAutoAssignResource: The parsed response data.
        """
        return self._parse_one(
            BoardAutoAssignResource,
            super()._make_request("POST", data=data, params=params).json(),
        )
