from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMembersTypesIdEndpoint import SystemMembersTypesIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesCountEndpoint import SystemMembersTypesCountEndpoint
from pyconnectwise.endpoints.manage.SystemMembersTypesInfoEndpoint import SystemMembersTypesInfoEndpoint
from pyconnectwise.models.manage.MemberTypeModel import MemberTypeModel

class SystemMembersTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemMembersTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMembersTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersTypesIdEndpoint: The initialized SystemMembersTypesIdEndpoint object.
        """
        child = SystemMembersTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberTypeModel]:
        """
        Performs a GET request against the /system/members/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberTypeModel]:
        """
        Performs a GET request against the /system/members/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberTypeModel]: The parsed response data.
        """
        return self._parse_many(MemberTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberTypeModel:
        """
        Performs a POST request against the /system/members/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberTypeModel: The parsed response data.
        """
        return self._parse_one(MemberTypeModel, super().make_request("POST", params=params).json())
        