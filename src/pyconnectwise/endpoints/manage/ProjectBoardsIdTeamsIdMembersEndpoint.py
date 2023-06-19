from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdMembersIdEndpoint import ProjectBoardsIdTeamsIdMembersIdEndpoint
from pyconnectwise.models.manage.ProjectBoardTeamMemberModel import ProjectBoardTeamMemberModel

class ProjectBoardsIdTeamsIdMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
    
    
    def id(self, id: int) -> ProjectBoardsIdTeamsIdMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdTeamsIdMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBoardsIdTeamsIdMembersIdEndpoint: The initialized ProjectBoardsIdTeamsIdMembersIdEndpoint object.
        """
        child = ProjectBoardsIdTeamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectBoardTeamMemberModel]:
        """
        Performs a GET request against the /project/boards/{grandparentId}/teams/{parentId}/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBoardTeamMemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectBoardTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectBoardTeamMemberModel]:
        """
        Performs a GET request against the /project/boards/{grandparentId}/teams/{parentId}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBoardTeamMemberModel]: The parsed response data.
        """
        return self._parse_many(ProjectBoardTeamMemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamMemberModel:
        """
        Performs a POST request against the /project/boards/{grandparentId}/teams/{parentId}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamMemberModel: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamMemberModel, super().make_request("POST", params=params).json())
        