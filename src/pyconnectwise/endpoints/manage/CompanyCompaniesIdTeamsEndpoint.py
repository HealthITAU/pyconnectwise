from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsIdEndpoint import CompanyCompaniesIdTeamsIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsCountEndpoint import CompanyCompaniesIdTeamsCountEndpoint
from pyconnectwise.models.manage.CompanyTeamModel import CompanyTeamModel

class CompanyCompaniesIdTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "teams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdTeamsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompaniesIdTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompaniesIdTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompaniesIdTeamsIdEndpoint: The initialized CompanyCompaniesIdTeamsIdEndpoint object.
        """
        child = CompanyCompaniesIdTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyTeamModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/teams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyTeamModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyTeamModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyTeamModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyTeamModel]: The parsed response data.
        """
        return self._parse_many(CompanyTeamModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyTeamModel:
        """
        Performs a POST request against the /company/companies/{parentId}/teams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyTeamModel: The parsed response data.
        """
        return self._parse_one(CompanyTeamModel, super().make_request("POST", params=params).json())
        