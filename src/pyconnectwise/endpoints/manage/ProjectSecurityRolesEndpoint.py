from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectSecurityRolesIdEndpoint import ProjectSecurityRolesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityRolesCountEndpoint import ProjectSecurityRolesCountEndpoint
from pyconnectwise.models.manage.ProjectSecurityRoleModel import ProjectSecurityRoleModel

class ProjectSecurityRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "securityRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectSecurityRolesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectSecurityRolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectSecurityRolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectSecurityRolesIdEndpoint: The initialized ProjectSecurityRolesIdEndpoint object.
        """
        child = ProjectSecurityRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectSecurityRoleModel]:
        """
        Performs a GET request against the /project/securityRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectSecurityRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectSecurityRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectSecurityRoleModel]:
        """
        Performs a GET request against the /project/securityRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectSecurityRoleModel]: The parsed response data.
        """
        return self._parse_many(ProjectSecurityRoleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectSecurityRoleModel:
        """
        Performs a POST request against the /project/securityRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectSecurityRoleModel: The parsed response data.
        """
        return self._parse_one(ProjectSecurityRoleModel, super().make_request("POST", params=params).json())
        