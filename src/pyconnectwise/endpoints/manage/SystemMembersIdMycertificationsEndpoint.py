from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdMycertificationsCountEndpoint import \
    SystemMembersIdMycertificationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdMycertificationsIdEndpoint import \
    SystemMembersIdMycertificationsIdEndpoint
from pyconnectwise.models.manage import MemberCertification
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdMycertificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "mycertifications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemMembersIdMycertificationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMembersIdMycertificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdMycertificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdMycertificationsIdEndpoint: The initialized SystemMembersIdMycertificationsIdEndpoint object.
        """
        child = SystemMembersIdMycertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[MemberCertification]:
        """
        Performs a GET request against the /system/members/{id}/mycertifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberCertification]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), MemberCertification, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberCertification]:
        """
        Performs a GET request against the /system/members/{id}/mycertifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberCertification]: The parsed response data.
        """
        return self._parse_many(MemberCertification, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberCertification:
        """
        Performs a POST request against the /system/members/{id}/mycertifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberCertification: The parsed response data.
        """
        return self._parse_one(MemberCertification, super()._make_request("POST", data=data, params=params).json())
