from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMembersIdEndpoint import SystemMembersIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdEndpoint import SystemMembersIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersCountEndpoint import SystemMembersCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesEndpoint import SystemMembersTypesEndpoint
from pyconnectwise.endpoints.manage.SystemMembersWithSsoEndpoint import SystemMembersWithSsoEndpoint
from pyconnectwise.models.manage.MemberModel import MemberModel

class SystemMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            SystemMembersTypesEndpoint(client, parent_endpoint=self)
        )
        self.withSso = self.register_child_endpoint(
            SystemMembersWithSsoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdEndpoint: The initialized SystemMembersIdEndpoint object.
        """
        child = SystemMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberModel]:
        """
        Performs a GET request against the /system/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberModel]:
        """
        Performs a GET request against the /system/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberModel]: The parsed response data.
        """
        return self._parse_many(MemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberModel:
        """
        Performs a POST request against the /system/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberModel: The parsed response data.
        """
        return self._parse_one(MemberModel, super().make_request("POST", params=params).json())
        