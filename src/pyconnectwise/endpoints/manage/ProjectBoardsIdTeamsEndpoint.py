from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdEndpoint import ProjectBoardsIdTeamsIdEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsCountEndpoint import ProjectBoardsIdTeamsCountEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsInfoEndpoint import ProjectBoardsIdTeamsInfoEndpoint
from pyconnectwise.models.manage.ProjectBoardTeamModel import ProjectBoardTeamModel

class ProjectBoardsIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectBoardsIdTeamsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectBoardsIdTeamsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectBoardsIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectBoardsIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectBoardsIdTeamsIdEndpoint: The initialized ProjectBoardsIdTeamsIdEndpoint object.
        """
        child = ProjectBoardsIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectBoardTeamModel]:
        """
        Performs a GET request against the /project/boards/{parentId}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectBoardTeamModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectBoardTeamModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectBoardTeamModel]:
        """
        Performs a GET request against the /project/boards/{parentId}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectBoardTeamModel]: The parsed response data.
        """
        return self._parse_many(ProjectBoardTeamModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamModel:
        """
        Performs a POST request against the /project/boards/{parentId}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamModel: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamModel, super().make_request("POST", params=params).json())
        