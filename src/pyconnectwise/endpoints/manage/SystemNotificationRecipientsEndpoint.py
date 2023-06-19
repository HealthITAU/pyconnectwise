from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemNotificationRecipientsIdEndpoint import SystemNotificationRecipientsIdEndpoint
from pyconnectwise.endpoints.manage.SystemNotificationRecipientsCountEndpoint import SystemNotificationRecipientsCountEndpoint
from pyconnectwise.models.manage.NotificationRecipientModel import NotificationRecipientModel

class SystemNotificationRecipientsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notificationRecipients", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemNotificationRecipientsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemNotificationRecipientsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemNotificationRecipientsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemNotificationRecipientsIdEndpoint: The initialized SystemNotificationRecipientsIdEndpoint object.
        """
        child = SystemNotificationRecipientsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[NotificationRecipientModel]:
        """
        Performs a GET request against the /system/notificationRecipients endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[NotificationRecipientModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            NotificationRecipientModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[NotificationRecipientModel]:
        """
        Performs a GET request against the /system/notificationRecipients endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[NotificationRecipientModel]: The parsed response data.
        """
        return self._parse_many(NotificationRecipientModel, super().make_request("GET", params=params).json())
        