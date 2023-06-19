from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyTeamRolesIdEndpoint import CompanyTeamRolesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyTeamRolesCountEndpoint import CompanyTeamRolesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyTeamRolesInfoEndpoint import CompanyTeamRolesInfoEndpoint
from pyconnectwise.models.manage.TeamRoleModel import TeamRoleModel

class CompanyTeamRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teamRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTeamRolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyTeamRolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyTeamRolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyTeamRolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyTeamRolesIdEndpoint: The initialized CompanyTeamRolesIdEndpoint object.
        """
        child = CompanyTeamRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TeamRoleModel]:
        """
        Performs a GET request against the /company/teamRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TeamRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TeamRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TeamRoleModel]:
        """
        Performs a GET request against the /company/teamRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TeamRoleModel]: The parsed response data.
        """
        return self._parse_many(TeamRoleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TeamRoleModel:
        """
        Performs a POST request against the /company/teamRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TeamRoleModel: The parsed response data.
        """
        return self._parse_one(TeamRoleModel, super().make_request("POST", params=params).json())
        