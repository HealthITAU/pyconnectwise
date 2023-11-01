from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdAccrualsCountEndpoint import (
    SystemMembersIdAccrualsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMembersIdAccrualsIdEndpoint import (
    SystemMembersIdAccrualsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import MemberAccrual
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMembersIdAccrualsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberAccrual], ConnectWiseManageRequestParams],
    IPostable[MemberAccrual, ConnectWiseManageRequestParams],
    IPaginateable[MemberAccrual, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "accruals", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[MemberAccrual])
        IPostable.__init__(self, MemberAccrual)
        IPaginateable.__init__(self, MemberAccrual)

        self.count = self._register_child_endpoint(
            SystemMembersIdAccrualsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMembersIdAccrualsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdAccrualsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdAccrualsIdEndpoint: The initialized SystemMembersIdAccrualsIdEndpoint object.
        """
        child = SystemMembersIdAccrualsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MemberAccrual]:
        """
        Performs a GET request against the /system/members/{id}/accruals endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberAccrual]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MemberAccrual,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[MemberAccrual]:
        """
        Performs a GET request against the /system/members/{id}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberAccrual]: The parsed response data.
        """
        return self._parse_many(
            MemberAccrual, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberAccrual:
        """
        Performs a POST request against the /system/members/{id}/accruals endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberAccrual: The parsed response data.
        """
        return self._parse_one(
            MemberAccrual,
            super()._make_request("POST", data=data, params=params).json(),
        )
