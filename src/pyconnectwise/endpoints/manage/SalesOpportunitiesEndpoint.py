from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdEndpoint import SalesOpportunitiesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesCountEndpoint import SalesOpportunitiesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesDefaultEndpoint import SalesOpportunitiesDefaultEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsEndpoint import SalesOpportunitiesRatingsEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesStatusesEndpoint import SalesOpportunitiesStatusesEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesEndpoint import SalesOpportunitiesTypesEndpoint
from pyconnectwise.models.manage.OpportunityModel import OpportunityModel

class SalesOpportunitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            SalesOpportunitiesDefaultEndpoint(client, parent_endpoint=self)
        )
        self.ratings = self.register_child_endpoint(
            SalesOpportunitiesRatingsEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            SalesOpportunitiesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            SalesOpportunitiesTypesEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOpportunitiesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdEndpoint: The initialized SalesOpportunitiesIdEndpoint object.
        """
        child = SalesOpportunitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityModel]:
        """
        Performs a GET request against the /sales/opportunities endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityModel]:
        """
        Performs a GET request against the /sales/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityModel]: The parsed response data.
        """
        return self._parse_many(OpportunityModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityModel:
        """
        Performs a POST request against the /sales/opportunities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityModel: The parsed response data.
        """
        return self._parse_one(OpportunityModel, super().make_request("POST", params=params).json())
        