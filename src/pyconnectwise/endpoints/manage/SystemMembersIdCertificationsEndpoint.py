from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMembersIdCertificationsIdEndpoint import SystemMembersIdCertificationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdCertificationsCountEndpoint import SystemMembersIdCertificationsCountEndpoint
from pyconnectwise.models.manage.MemberCertificationModel import MemberCertificationModel

class SystemMembersIdCertificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "certifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdCertificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMembersIdCertificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMembersIdCertificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMembersIdCertificationsIdEndpoint: The initialized SystemMembersIdCertificationsIdEndpoint object.
        """
        child = SystemMembersIdCertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberCertificationModel]:
        """
        Performs a GET request against the /system/members/{parentId}/certifications endpoint and returns an initialized PaginatedResponse object.

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
        Performs a GET request against the /system/members/{parentId}/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberCertificationModel]: The parsed response data.
        """
        return self._parse_many(MemberCertificationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberCertificationModel:
        """
        Performs a POST request against the /system/members/{parentId}/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberCertificationModel: The parsed response data.
        """
        return self._parse_one(MemberCertificationModel, super().make_request("POST", params=params).json())
        