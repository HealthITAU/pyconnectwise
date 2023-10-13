from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesCountEndpoint import SystemMembersTypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesIdEndpoint import SystemMembersTypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesInfoEndpoint import SystemMembersTypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import MemberType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMembersTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberType], ConnectWiseManageRequestParams],
    IPostable[MemberType, ConnectWiseManageRequestParams],
    IPaginateable[MemberType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[MemberType])
        IPostable.__init__(self, MemberType)
        IPaginateable.__init__(self, MemberType)

        self.count = self._register_child_endpoint(SystemMembersTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemMembersTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemMembersTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersTypesIdEndpoint: The initialized SystemMembersTypesIdEndpoint object.
        """
        child = SystemMembersTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[MemberType]:
        """
        Performs a GET request against the /system/members/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), MemberType, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[MemberType]:
        """
        Performs a GET request against the /system/members/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberType]: The parsed response data.
        """
        return self._parse_many(MemberType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> MemberType:
        """
        Performs a POST request against the /system/members/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberType: The parsed response data.
        """
        return self._parse_one(MemberType, super()._make_request("POST", data=data, params=params).json())
