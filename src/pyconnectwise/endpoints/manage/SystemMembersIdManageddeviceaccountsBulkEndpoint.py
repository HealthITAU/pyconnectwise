from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.manage import BulkResult
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdManageddeviceaccountsBulkEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bulk", parent_endpoint=parent_endpoint)

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BulkResult:
        """
        Performs a DELETE request against the /system/members/{id}/managedDeviceAccounts/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("DELETE", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BulkResult:
        """
        Performs a PUT request against the /system/members/{id}/managedDeviceAccounts/bulk endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BulkResult: The parsed response data.
        """
        return self._parse_one(BulkResult, super()._make_request("PUT", data=data, params=params).json())
