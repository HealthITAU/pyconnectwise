from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesInfoCountEndpoint import (
    ServiceBoardsIdSubtypesInfoCountEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import BoardSubTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceBoardsIdSubtypesInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[BoardSubTypeInfo], ConnectWiseManageRequestParams],
    IPaginateable[BoardSubTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[BoardSubTypeInfo])
        IPaginateable.__init__(self, BoardSubTypeInfo)

        self.count = self._register_child_endpoint(
            ServiceBoardsIdSubtypesInfoCountEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[BoardSubTypeInfo]:
        """
        Performs a GET request against the /service/boards/{id}/subtypes/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardSubTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), BoardSubTypeInfo, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[BoardSubTypeInfo]:
        """
        Performs a GET request against the /service/boards/{id}/subtypes/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardSubTypeInfo]: The parsed response data.
        """
        return self._parse_many(BoardSubTypeInfo, super()._make_request("GET", data=data, params=params).json())
