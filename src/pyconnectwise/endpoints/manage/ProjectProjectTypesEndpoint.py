from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProjectProjectTypesIdEndpoint import ProjectProjectTypesIdEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectTypesCountEndpoint import ProjectProjectTypesCountEndpoint
from pyconnectwise.endpoints.manage.ProjectProjectTypesInfoEndpoint import ProjectProjectTypesInfoEndpoint
from pyconnectwise.models.manage.ProjectTypeModel import ProjectTypeModel

class ProjectProjectTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectProjectTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProjectProjectTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProjectProjectTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProjectProjectTypesIdEndpoint: The initialized ProjectProjectTypesIdEndpoint object.
        """
        child = ProjectProjectTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProjectTypeModel]:
        """
        Performs a GET request against the /project/projectTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProjectTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProjectTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProjectTypeModel]:
        """
        Performs a GET request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProjectTypeModel]: The parsed response data.
        """
        return self._parse_many(ProjectTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProjectTypeModel:
        """
        Performs a POST request against the /project/projectTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProjectTypeModel: The parsed response data.
        """
        return self._parse_one(ProjectTypeModel, super().make_request("POST", params=params).json())
        