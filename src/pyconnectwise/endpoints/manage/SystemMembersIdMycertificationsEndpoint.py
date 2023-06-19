from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMembersIdMycertificationsIdEndpoint import SystemMembersIdMycertificationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdMycertificationsCountEndpoint import SystemMembersIdMycertificationsCountEndpoint
from pyconnectwise.models.manage.MemberCertificationModel import MemberCertificationModel

class SystemMembersIdMycertificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "mycertifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdMycertificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMembersIdMycertificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdMycertificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdMycertificationsIdEndpoint: The initialized SystemMembersIdMycertificationsIdEndpoint object.
        """
        child = SystemMembersIdMycertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberCertificationModel]:
        """
        Performs a GET request against the /system/members/{parentId}/mycertifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberCertificationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberCertificationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberCertificationModel]:
        """
        Performs a GET request against the /system/members/{parentId}/mycertifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberCertificationModel]: The parsed response data.
        """
        return self._parse_many(MemberCertificationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberCertificationModel:
        """
        Performs a POST request against the /system/members/{parentId}/mycertifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberCertificationModel: The parsed response data.
        """
        return self._parse_one(MemberCertificationModel, super().make_request("POST", params=params).json())
        