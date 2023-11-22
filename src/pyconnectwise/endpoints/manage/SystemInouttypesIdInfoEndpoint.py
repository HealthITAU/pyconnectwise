from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import InOutTypeInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemInouttypesIdInfoEndpoint(
    ConnectWiseEndpoint,
    IGettable[InOutTypeInfo, ConnectWiseManageRequestParams],
    IPaginateable[InOutTypeInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "info", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, InOutTypeInfo)
        IPaginateable.__init__(self, InOutTypeInfo)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[InOutTypeInfo]:
        """
        Performs a GET request against the /system/inOutTypes/{id}/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InOutTypeInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), InOutTypeInfo, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> InOutTypeInfo:
        """
        Performs a GET request against the /system/inOutTypes/{id}/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InOutTypeInfo: The parsed response data.
        """
        return self._parse_one(InOutTypeInfo, super()._make_request("GET", data=data, params=params).json())
