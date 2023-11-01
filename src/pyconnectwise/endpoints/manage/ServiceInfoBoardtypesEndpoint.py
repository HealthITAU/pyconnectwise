from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesCountEndpoint import (
    ServiceInfoBoardtypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceInfoBoardtypesIdEndpoint import (
    ServiceInfoBoardtypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import BoardTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceInfoBoardtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[BoardTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "boardtypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[BoardTypeInfo])
        IPaginateable.__init__(self, BoardTypeInfo)

        self.count = self._register_child_endpoint(
            ServiceInfoBoardtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceInfoBoardtypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ServiceInfoBoardtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceInfoBoardtypesIdEndpoint: The initialized ServiceInfoBoardtypesIdEndpoint object.
        """
        child = ServiceInfoBoardtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardTypeInfo]:
        """
        Performs a GET request against the /service/info/boardtypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardTypeInfo,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[BoardTypeInfo]:
        """
        Performs a GET request against the /service/info/boardtypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardTypeInfo]: The parsed response data.
        """
        return self._parse_many(
            BoardTypeInfo, super()._make_request("GET", data=data, params=params).json()
        )
