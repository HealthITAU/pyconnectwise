from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationrecipientsCountEndpoint import \
    SystemNotificationrecipientsCountEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationrecipientsIdEndpoint import SystemNotificationrecipientsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import NotificationRecipient
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemNotificationrecipientsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[NotificationRecipient], ConnectWiseManageRequestParams],
    IPaginateable[NotificationRecipient, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "notificationRecipients", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[NotificationRecipient])
        IPaginateable.__init__(self, NotificationRecipient)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), NotificationRecipient, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[NotificationRecipient]:
        """
        Performs a GET request against the /system/notificationRecipients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[NotificationRecipient]: The parsed response data.
        """
        return self._parse_many(NotificationRecipient, super()._make_request("GET", data=data, params=params).json())
