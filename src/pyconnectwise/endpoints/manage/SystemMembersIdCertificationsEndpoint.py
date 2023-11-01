from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdCertificationsCountEndpoint import (
    SystemMembersIdCertificationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMembersIdCertificationsIdEndpoint import (
    SystemMembersIdCertificationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import MemberCertification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMembersIdCertificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberCertification], ConnectWiseManageRequestParams],
    IPostable[MemberCertification, ConnectWiseManageRequestParams],
    IPaginateable[MemberCertification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "certifications", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[MemberCertification])
        IPostable.__init__(self, MemberCertification)
        IPaginateable.__init__(self, MemberCertification)

        self.count = self._register_child_endpoint(
            SystemMembersIdCertificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMembersIdCertificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdCertificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdCertificationsIdEndpoint: The initialized SystemMembersIdCertificationsIdEndpoint object.
        """
        child = SystemMembersIdCertificationsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MemberCertification]:
        """
        Performs a GET request against the /system/members/{id}/certifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberCertification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MemberCertification,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[MemberCertification]:
        """
        Performs a GET request against the /system/members/{id}/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberCertification]: The parsed response data.
        """
        return self._parse_many(
            MemberCertification,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberCertification:
        """
        Performs a POST request against the /system/members/{id}/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberCertification: The parsed response data.
        """
        return self._parse_one(
            MemberCertification,
            super()._make_request("POST", data=data, params=params).json(),
        )
