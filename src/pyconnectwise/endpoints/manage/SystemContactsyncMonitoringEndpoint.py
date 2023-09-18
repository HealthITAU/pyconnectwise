from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringCountEndpoint import \
    SystemContactsyncMonitoringCountEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringIdEndpoint import SystemContactsyncMonitoringIdEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringNotificationtypeEndpoint import \
    SystemContactsyncMonitoringNotificationtypeEndpoint
from pyconnectwise.endpoints.manage.SystemContactsyncMonitoringTypeEndpoint import \
    SystemContactsyncMonitoringTypeEndpoint
from pyconnectwise.models.manage import M365ContactSyncMonitoring
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemContactsyncMonitoringEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "monitoring", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemContactsyncMonitoringCountEndpoint(client, parent_endpoint=self)
        )
        self.type = self._register_child_endpoint(SystemContactsyncMonitoringTypeEndpoint(client, parent_endpoint=self))
        self.notificationtype = self._register_child_endpoint(
            SystemContactsyncMonitoringNotificationtypeEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemContactsyncMonitoringIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemContactsyncMonitoringIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemContactsyncMonitoringIdEndpoint: The initialized SystemContactsyncMonitoringIdEndpoint object.
        """
        child = SystemContactsyncMonitoringIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[M365ContactSyncMonitoring]:
        """
        Performs a GET request against the /system/contactsync/monitoring endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[M365ContactSyncMonitoring]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), M365ContactSyncMonitoring, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[M365ContactSyncMonitoring]:
        """
        Performs a GET request against the /system/contactsync/monitoring endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[M365ContactSyncMonitoring]: The parsed response data.
        """
        return self._parse_many(
            M365ContactSyncMonitoring, super()._make_request("GET", data=data, params=params).json()
        )
