from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemApiMembersIdEndpoint import SystemApiMembersIdEndpoint
from pyconnectwise.endpoints.manage.SystemApiMembersCountEndpoint import SystemApiMembersCountEndpoint
from pyconnectwise.endpoints.manage.SystemApiMembersDefaultEndpoint import SystemApiMembersDefaultEndpoint
from pyconnectwise.models.manage.ApiMemberModel import ApiMemberModel

class SystemApiMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "apiMembers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemApiMembersCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            SystemApiMembersDefaultEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemApiMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemApiMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemApiMembersIdEndpoint: The initialized SystemApiMembersIdEndpoint object.
        """
        child = SystemApiMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ApiMemberModel]:
        """
        Performs a GET request against the /system/apiMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ApiMemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ApiMemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ApiMemberModel]:
        """
        Performs a GET request against the /system/apiMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ApiMemberModel]: The parsed response data.
        """
        return self._parse_many(ApiMemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ApiMemberModel:
        """
        Performs a POST request against the /system/apiMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ApiMemberModel: The parsed response data.
        """
        return self._parse_one(ApiMemberModel, super().make_request("POST", params=params).json())
        