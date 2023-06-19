from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.BulkResultModel import BulkResultModel

class SystemMembersIdManagedDeviceAccountsBulkEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bulk", parent_endpoint=parent_endpoint)
        
    
    
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BulkResultModel:
        """
        Performs a DELETE request against the /system/members/{parentId}/managedDeviceAccounts/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResultModel: The parsed response data.
        """
        return self._parse_one(BulkResultModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BulkResultModel:
        """
        Performs a PUT request against the /system/members/{parentId}/managedDeviceAccounts/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResultModel: The parsed response data.
        """
        return self._parse_one(BulkResultModel, super().make_request("PUT", params=params).json())
        