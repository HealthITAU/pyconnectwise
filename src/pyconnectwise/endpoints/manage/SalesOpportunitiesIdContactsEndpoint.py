from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsIdEndpoint import SalesOpportunitiesIdContactsIdEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsCountEndpoint import SalesOpportunitiesIdContactsCountEndpoint
from pyconnectwise.models.manage.OpportunityContactModel import OpportunityContactModel

class SalesOpportunitiesIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdContactsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesOpportunitiesIdContactsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesIdContactsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesOpportunitiesIdContactsIdEndpoint: The initialized SalesOpportunitiesIdContactsIdEndpoint object.
        """
        child = SalesOpportunitiesIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OpportunityContactModel]:
        """
        Performs a GET request against the /sales/opportunities/{parentId}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OpportunityContactModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OpportunityContactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OpportunityContactModel]:
        """
        Performs a GET request against the /sales/opportunities/{parentId}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OpportunityContactModel]: The parsed response data.
        """
        return self._parse_many(OpportunityContactModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> OpportunityContactModel:
        """
        Performs a POST request against the /sales/opportunities/{parentId}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityContactModel: The parsed response data.
        """
        return self._parse_one(OpportunityContactModel, super().make_request("POST", params=params).json())
        