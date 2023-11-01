from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdNotificationsettingsCountEndpoint import (
    SystemMembersIdNotificationsettingsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMembersIdNotificationsettingsIdEndpoint import (
    SystemMembersIdNotificationsettingsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import MemberNotificationSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMembersIdNotificationsettingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[MemberNotificationSetting], ConnectWiseManageRequestParams],
    IPostable[MemberNotificationSetting, ConnectWiseManageRequestParams],
    IPaginateable[MemberNotificationSetting, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "notificationSettings", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[MemberNotificationSetting])
        IPostable.__init__(self, MemberNotificationSetting)
        IPaginateable.__init__(self, MemberNotificationSetting)

        self.count = self._register_child_endpoint(
            SystemMembersIdNotificationsettingsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> SystemMembersIdNotificationsettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdNotificationsettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdNotificationsettingsIdEndpoint: The initialized SystemMembersIdNotificationsettingsIdEndpoint object.
        """
        child = SystemMembersIdNotificationsettingsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MemberNotificationSetting]:
        """
        Performs a GET request against the /system/members/{id}/notificationSettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberNotificationSetting]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MemberNotificationSetting,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[MemberNotificationSetting]:
        """
        Performs a GET request against the /system/members/{id}/notificationSettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberNotificationSetting]: The parsed response data.
        """
        return self._parse_many(
            MemberNotificationSetting,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberNotificationSetting:
        """
        Performs a POST request against the /system/members/{id}/notificationSettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberNotificationSetting: The parsed response data.
        """
        return self._parse_one(
            MemberNotificationSetting,
            super()._make_request("POST", data=data, params=params).json(),
        )
