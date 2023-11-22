from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesCountEndpoint import SystemInouttypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesIdEndpoint import SystemInouttypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemInouttypesInfoEndpoint import SystemInouttypesInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import InOutType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemInouttypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[InOutType], ConnectWiseManageRequestParams],
    IPostable[InOutType, ConnectWiseManageRequestParams],
    IPaginateable[InOutType, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "inOutTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[InOutType])
        IPostable.__init__(self, InOutType)
        IPaginateable.__init__(self, InOutType)

        self.count = self._register_child_endpoint(SystemInouttypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemInouttypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemInouttypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemInouttypesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemInouttypesIdEndpoint: The initialized SystemInouttypesIdEndpoint object.
        """
        child = SystemInouttypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[InOutType]:
        """
        Performs a GET request against the /system/inOutTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InOutType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), InOutType, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[InOutType]:
        """
        Performs a GET request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InOutType]: The parsed response data.
        """
        return self._parse_many(InOutType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> InOutType:
        """
        Performs a POST request against the /system/inOutTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            InOutType: The parsed response data.
        """
        return self._parse_one(InOutType, super()._make_request("POST", data=data, params=params).json())
