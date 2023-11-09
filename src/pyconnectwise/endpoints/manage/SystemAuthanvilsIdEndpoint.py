from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import AuthAnvil
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemAuthanvilsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[AuthAnvil, ConnectWiseManageRequestParams],
    IPatchable[AuthAnvil, ConnectWiseManageRequestParams],
    IPuttable[AuthAnvil, ConnectWiseManageRequestParams],
    IPaginateable[AuthAnvil, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, AuthAnvil)
        IPatchable.__init__(self, AuthAnvil)
        IPuttable.__init__(self, AuthAnvil)
        IPaginateable.__init__(self, AuthAnvil)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AuthAnvil]:
        """
        Performs a GET request against the /system/authAnvils/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AuthAnvil]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), AuthAnvil, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AuthAnvil:
        """
        Performs a GET request against the /system/authAnvils/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthAnvil: The parsed response data.
        """
        return self._parse_one(AuthAnvil, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> AuthAnvil:
        """
        Performs a PATCH request against the /system/authAnvils/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthAnvil: The parsed response data.
        """
        return self._parse_one(AuthAnvil, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AuthAnvil:
        """
        Performs a PUT request against the /system/authAnvils/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AuthAnvil: The parsed response data.
        """
        return self._parse_one(AuthAnvil, super()._make_request("PUT", data=data, params=params).json())
