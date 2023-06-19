from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdMembersEndpoint import ProjectBoardsIdTeamsIdMembersEndpoint
from pyconnectwise.endpoints.manage.ProjectBoardsIdTeamsIdInfoEndpoint import ProjectBoardsIdTeamsIdInfoEndpoint
from pyconnectwise.models.manage.ProjectBoardTeamModel import ProjectBoardTeamModel

class ProjectBoardsIdTeamsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.members = self.register_child_endpoint(
            ProjectBoardsIdTeamsIdMembersEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectBoardsIdTeamsIdInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectBoardTeamModel]:
        """
        Performs a GET request against the /project/boards/{parentId}/teams/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamModel:
        """
        Performs a GET request against the /project/boards/{parentId}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamModel: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /project/boards/{parentId}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamModel:
        """
        Performs a PUT request against the /project/boards/{parentId}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamModel: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectBoardTeamModel:
        """
        Performs a PATCH request against the /project/boards/{parentId}/teams/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectBoardTeamModel: The parsed response data.
        """
        return self._parse_one(ProjectBoardTeamModel, super().make_request("PATCH", params=params).json())
        