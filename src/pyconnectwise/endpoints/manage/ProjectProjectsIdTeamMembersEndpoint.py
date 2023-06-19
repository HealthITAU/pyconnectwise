from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeamMembersIdEndpoint import ProjectProjectsIdTeamMembersIdEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeamMembersCountEndpoint import ProjectProjectsIdTeamMembersCountEndpoint
from pyconnectwise.models.manage.ProjectTeamMemberModel import ProjectTeamMemberModel

class ProjectProjectsIdTeamMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teamMembers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdTeamMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectProjectsIdTeamMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdTeamMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdTeamMembersIdEndpoint: The initialized ProjectProjectsIdTeamMembersIdEndpoint object.
        """
        child = ProjectProjectsIdTeamMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectTeamMemberModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/teamMembers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTeamMemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectTeamMemberModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/teamMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTeamMemberModel]: The parsed response data.
        """
        return self._parse_many(ProjectTeamMemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTeamMemberModel:
        """
        Performs a POST request against the /project/projects/{parentId}/teamMembers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTeamMemberModel: The parsed response data.
        """
        return self._parse_one(ProjectTeamMemberModel, super().make_request("POST", params=params).json())
        