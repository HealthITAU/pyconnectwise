from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesIdEndpoint import ProjectProjectsIdNotesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesCountEndpoint import ProjectProjectsIdNotesCountEndpoint
from pyconnectwise.models.manage.ProjectNoteModel import ProjectNoteModel

class ProjectProjectsIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectsIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectProjectsIdNotesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectsIdNotesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectsIdNotesIdEndpoint: The initialized ProjectProjectsIdNotesIdEndpoint object.
        """
        child = ProjectProjectsIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectNoteModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/notes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectNoteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectNoteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectNoteModel]:
        """
        Performs a GET request against the /project/projects/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectNoteModel]: The parsed response data.
        """
        return self._parse_many(ProjectNoteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectNoteModel:
        """
        Performs a POST request against the /project/projects/{parentId}/notes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectNoteModel: The parsed response data.
        """
        return self._parse_one(ProjectNoteModel, super().make_request("POST", params=params).json())
        