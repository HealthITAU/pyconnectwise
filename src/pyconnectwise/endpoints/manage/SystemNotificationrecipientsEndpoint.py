from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationrecipientsCountEndpoint import \
    SystemNotificationrecipientsCountEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationrecipientsIdEndpoint import SystemNotificationrecipientsIdEndpoint
from pyconnectwise.models.manage import NotificationRecipient
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemNotificationrecipientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notificationRecipients", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemNotificationrecipientsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemNotificationrecipientsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemNotificationrecipientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemNotificationrecipientsIdEndpoint: The initialized SystemNotificationrecipientsIdEndpoint object.
        """
        child = SystemNotificationrecipientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[NotificationRecipient]:
        """
        Performs a GET request against the /system/notificationRecipients endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[NotificationRecipient]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), NotificationRecipient, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[NotificationRecipient]:
        """
        Performs a GET request against the /system/notificationRecipients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[NotificationRecipient]: The parsed response data.
        """
        return self._parse_many(NotificationRecipient, super()._make_request("GET", data=data, params=params).json())
