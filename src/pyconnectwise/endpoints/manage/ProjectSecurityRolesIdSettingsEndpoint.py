from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectSecurityRolesIdSettingsIdEndpoint import ProjectSecurityRolesIdSettingsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectSecurityRolesIdSettingsCountEndpoint import ProjectSecurityRolesIdSettingsCountEndpoint
from pyconnectwise.models.manage.ProjectSecurityRoleSettingModel import ProjectSecurityRoleSettingModel

class ProjectSecurityRolesIdSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectSecurityRolesIdSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectSecurityRolesIdSettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectSecurityRolesIdSettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectSecurityRolesIdSettingsIdEndpoint: The initialized ProjectSecurityRolesIdSettingsIdEndpoint object.
        """
        child = ProjectSecurityRolesIdSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectSecurityRoleSettingModel]:
        """
        Performs a GET request against the /project/securityRoles/{parentId}/settings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectSecurityRoleSettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectSecurityRoleSettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectSecurityRoleSettingModel]:
        """
        Performs a GET request against the /project/securityRoles/{parentId}/settings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectSecurityRoleSettingModel]: The parsed response data.
        """
        return self._parse_many(ProjectSecurityRoleSettingModel, super().make_request("GET", params=params).json())
        