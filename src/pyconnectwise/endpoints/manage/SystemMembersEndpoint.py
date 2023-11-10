from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersCountEndpoint import SystemMembersCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdEndpoint import SystemMembersIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesEndpoint import SystemMembersTypesEndpoint
from pyconnectwise.endpoints.manage.SystemMembersWithssoEndpoint import SystemMembersWithssoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import Member
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemMembersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Member], ConnectWiseManageRequestParams],
    IPostable[Member, ConnectWiseManageRequestParams],
    IPaginateable[Member, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "members", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Member])
        IPostable.__init__(self, Member)
        IPaginateable.__init__(self, Member)

        self.count = self._register_child_endpoint(SystemMembersCountEndpoint(client, parent_endpoint=self))
        self.types = self._register_child_endpoint(SystemMembersTypesEndpoint(client, parent_endpoint=self))
        self.with_sso = self._register_child_endpoint(SystemMembersWithssoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> SystemMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SystemMembersIdEndpoint: The initialized SystemMembersIdEndpoint object.
        """
        child = SystemMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Member]:
        """
        Performs a GET request against the /system/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Member]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Member, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Member]:
        """
        Performs a GET request against the /system/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Member]: The parsed response data.
        """
        return self._parse_many(Member, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Member:
        """
        Performs a POST request against the /system/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Member: The parsed response data.
        """
        return self._parse_one(Member, super()._make_request("POST", data=data, params=params).json())
