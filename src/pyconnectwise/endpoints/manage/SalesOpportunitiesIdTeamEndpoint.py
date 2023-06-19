from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamIdEndpoint import SalesOpportunitiesIdTeamIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamCountEndpoint import SalesOpportunitiesIdTeamCountEndpoint
from pyconnectwise.models.manage.TeamModel import TeamModel

class SalesOpportunitiesIdTeamEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "team", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdTeamCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOpportunitiesIdTeamIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdTeamIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdTeamIdEndpoint: The initialized SalesOpportunitiesIdTeamIdEndpoint object.
        """
        child = SalesOpportunitiesIdTeamIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TeamModel]:
        """
        Performs a GET request against the /sales/opportunities/{parentId}/team endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TeamModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TeamModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TeamModel]:
        """
        Performs a GET request against the /sales/opportunities/{parentId}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TeamModel]: The parsed response data.
        """
        return self._parse_many(TeamModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TeamModel:
        """
        Performs a POST request against the /sales/opportunities/{parentId}/team endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TeamModel: The parsed response data.
        """
        return self._parse_one(TeamModel, super().make_request("POST", params=params).json())
        