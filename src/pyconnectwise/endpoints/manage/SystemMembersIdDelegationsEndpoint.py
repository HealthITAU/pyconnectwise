from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdDelegationsCountEndpoint import \
    SystemMembersIdDelegationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdDelegationsIdEndpoint import SystemMembersIdDelegationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import MemberDelegation
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMembersIdDelegationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberDelegation], ConnectWiseManageRequestParams],
    IPostable[MemberDelegation, ConnectWiseManageRequestParams],
    IPaginateable[MemberDelegation, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "delegations", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[MemberDelegation])
        IPostable.__init__(self, MemberDelegation)
        IPaginateable.__init__(self, MemberDelegation)

        self.count = self._register_child_endpoint(
            SystemMembersIdDelegationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMembersIdDelegationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdDelegationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdDelegationsIdEndpoint: The initialized SystemMembersIdDelegationsIdEndpoint object.
        """
        child = SystemMembersIdDelegationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[MemberDelegation]:
        """
        Performs a GET request against the /system/members/{id}/delegations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberDelegation]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberDelegation, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[MemberDelegation]:
        """
        Performs a GET request against the /system/members/{id}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberDelegation]: The parsed response data.
        """
        return self._parse_many(MemberDelegation, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> MemberDelegation:
        """
        Performs a POST request against the /system/members/{id}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberDelegation: The parsed response data.
        """
        return self._parse_one(MemberDelegation, super()._make_request("POST", data=data, params=params).json())
