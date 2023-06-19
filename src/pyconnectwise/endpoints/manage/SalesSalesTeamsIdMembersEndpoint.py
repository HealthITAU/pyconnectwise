from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesSalesTeamsIdMembersIdEndpoint import SalesSalesTeamsIdMembersIdEndpoint
from pyconnectwise.endpoints.manage.SalesSalesTeamsIdMembersCountEndpoint import SalesSalesTeamsIdMembersCountEndpoint
from pyconnectwise.models.manage.SalesTeamMemberModel import SalesTeamMemberModel

class SalesSalesTeamsIdMembersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "members", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesSalesTeamsIdMembersCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesSalesTeamsIdMembersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesSalesTeamsIdMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesSalesTeamsIdMembersIdEndpoint: The initialized SalesSalesTeamsIdMembersIdEndpoint object.
        """
        child = SalesSalesTeamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SalesTeamMemberModel]:
        """
        Performs a GET request against the /sales/salesTeams/{parentId}/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesTeamMemberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SalesTeamMemberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SalesTeamMemberModel]:
        """
        Performs a GET request against the /sales/salesTeams/{parentId}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesTeamMemberModel]: The parsed response data.
        """
        return self._parse_many(SalesTeamMemberModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SalesTeamMemberModel:
        """
        Performs a POST request against the /sales/salesTeams/{parentId}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesTeamMemberModel: The parsed response data.
        """
        return self._parse_one(SalesTeamMemberModel, super().make_request("POST", params=params).json())
        