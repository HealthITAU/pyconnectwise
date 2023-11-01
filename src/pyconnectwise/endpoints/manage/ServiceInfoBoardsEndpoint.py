from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardsCountEndpoint import (
    ServiceInfoBoardsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceInfoBoardsIdEndpoint import (
    ServiceInfoBoardsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import BoardInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceInfoBoardsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardInfo], ConnectWiseManageRequestParams],
    IPaginateable[BoardInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "boards", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BoardInfo])
        IPaginateable.__init__(self, BoardInfo)

        self.count = self._register_child_endpoint(
            ServiceInfoBoardsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceInfoBoardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceInfoBoardsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceInfoBoardsIdEndpoint: The initialized ServiceInfoBoardsIdEndpoint object.
        """
        child = ServiceInfoBoardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardInfo]:
        """
        Performs a GET request against the /service/info/boards endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BoardInfo]:
        """
        Performs a GET request against the /service/info/boards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardInfo]: The parsed response data.
        """
        return self._parse_many(
            BoardInfo, super()._make_request("GET", data=data, params=params).json()
        )
