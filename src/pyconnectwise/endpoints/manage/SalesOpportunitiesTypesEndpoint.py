from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesIdEndpoint import SalesOpportunitiesTypesIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesCountEndpoint import SalesOpportunitiesTypesCountEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesTypesInfoEndpoint import SalesOpportunitiesTypesInfoEndpoint
from pyconnectwise.models.manage.OpportunityTypeModel import OpportunityTypeModel

class SalesOpportunitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOpportunitiesTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOpportunitiesTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesTypesIdEndpoint: The initialized SalesOpportunitiesTypesIdEndpoint object.
        """
        child = SalesOpportunitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityTypeModel]:
        """
        Performs a GET request against the /sales/opportunities/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityTypeModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityTypeModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityTypeModel]:
        """
        Performs a GET request against the /sales/opportunities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityTypeModel]: The parsed response data.
        """
        return self._parse_many(OpportunityTypeModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityTypeModel:
        """
        Performs a POST request against the /sales/opportunities/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityTypeModel: The parsed response data.
        """
        return self._parse_one(OpportunityTypeModel, super().make_request("POST", params=params).json())
        