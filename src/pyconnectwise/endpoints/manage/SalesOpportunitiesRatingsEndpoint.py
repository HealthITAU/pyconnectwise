from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsIdEndpoint import SalesOpportunitiesRatingsIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsCountEndpoint import SalesOpportunitiesRatingsCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesRatingsInfoEndpoint import SalesOpportunitiesRatingsInfoEndpoint
from pyconnectwise.models.manage.OpportunityRatingModel import OpportunityRatingModel

class SalesOpportunitiesRatingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ratings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesRatingsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOpportunitiesRatingsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOpportunitiesRatingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesRatingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesRatingsIdEndpoint: The initialized SalesOpportunitiesRatingsIdEndpoint object.
        """
        child = SalesOpportunitiesRatingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityRatingModel]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityRatingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityRatingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityRatingModel]:
        """
        Performs a GET request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityRatingModel]: The parsed response data.
        """
        return self._parse_many(OpportunityRatingModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityRatingModel:
        """
        Performs a POST request against the /sales/opportunities/ratings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityRatingModel: The parsed response data.
        """
        return self._parse_one(OpportunityRatingModel, super().make_request("POST", params=params).json())
        