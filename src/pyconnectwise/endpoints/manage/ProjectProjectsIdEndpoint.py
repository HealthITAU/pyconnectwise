from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectProjectsIdContactsEndpoint import ProjectProjectsIdContactsEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdNotesEndpoint import ProjectProjectsIdNotesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdPhasesEndpoint import ProjectProjectsIdPhasesEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectsIdTeamMembersEndpoint import ProjectProjectsIdTeamMembersEndpoint
from pyconnectwise.models.manage.ProjectModel import ProjectModel

class ProjectProjectsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.contacts = self.register_child_endpoint(
            ProjectProjectsIdContactsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            ProjectProjectsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.phases = self.register_child_endpoint(
            ProjectProjectsIdPhasesEndpoint(client, parent_endpoint=self)
        )
        self.teamMembers = self.register_child_endpoint(
            ProjectProjectsIdTeamMembersEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectModel]:
        """
        Performs a GET request against the /project/projects/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectModel:
        """
        Performs a GET request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectModel: The parsed response data.
        """
        return self._parse_one(ProjectModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectModel:
        """
        Performs a PUT request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectModel: The parsed response data.
        """
        return self._parse_one(ProjectModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectModel:
        """
        Performs a PATCH request against the /project/projects/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectModel: The parsed response data.
        """
        return self._parse_one(ProjectModel, super().make_request("PATCH", params=params).json())
        