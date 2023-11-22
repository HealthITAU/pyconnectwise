from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInoutboardsCountEndpoint import SystemInoutboardsCountEndpoint
from pyconnectwise.endpoints.manage.SystemInoutboardsIdEndpoint import SystemInoutboardsIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import InOutBoard
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemInoutboardsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InOutBoard], ConnectWiseManageRequestParams],
    IPostable[InOutBoard, ConnectWiseManageRequestParams],
    IPaginateable[InOutBoard, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "inOutBoards", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[InOutBoard])
        IPostable.__init__(self, InOutBoard)
        IPaginateable.__init__(self, InOutBoard)

        self.count = self._register_child_endpoint(SystemInoutboardsCountEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemInoutboardsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInoutboardsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemInoutboardsIdEndpoint: The initialized SystemInoutboardsIdEndpoint object.
        """
        child = SystemInoutboardsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[InOutBoard]:
        """
        Performs a GET request against the /system/inOutBoards endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InOutBoard]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), InOutBoard, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[InOutBoard]:
        """
        Performs a GET request against the /system/inOutBoards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InOutBoard]: The parsed response data.
        """
        return self._parse_many(InOutBoard, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> InOutBoard:
        """
        Performs a POST request against the /system/inOutBoards endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InOutBoard: The parsed response data.
        """
        return self._parse_one(InOutBoard, super()._make_request("POST", data=data, params=params).json())
