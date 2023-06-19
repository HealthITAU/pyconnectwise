from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesSalesTeamsIdEndpoint import SalesSalesTeamsIdEndpoint
from pyconnectwise.endpoints.manage.SalesSalesTeamsCountEndpoint import SalesSalesTeamsCountEndpoint
from pyconnectwise.models.manage.SalesTeamModel import SalesTeamModel

class SalesSalesTeamsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "salesTeams", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesSalesTeamsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesSalesTeamsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesSalesTeamsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesSalesTeamsIdEndpoint: The initialized SalesSalesTeamsIdEndpoint object.
        """
        child = SalesSalesTeamsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SalesTeamModel]:
        """
        Performs a GET request against the /sales/salesTeams endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesTeamModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SalesTeamModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SalesTeamModel]:
        """
        Performs a GET request against the /sales/salesTeams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesTeamModel]: The parsed response data.
        """
        return self._parse_many(SalesTeamModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SalesTeamModel:
        """
        Performs a POST request against the /sales/salesTeams endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesTeamModel: The parsed response data.
        """
        return self._parse_one(SalesTeamModel, super().make_request("POST", params=params).json())
        