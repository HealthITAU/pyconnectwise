from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingGroupsIdEndpoint import MarketingGroupsIdEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsCountEndpoint import MarketingGroupsCountEndpoint
from pyconnectwise.models.manage.GroupModel import GroupModel

class MarketingGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> MarketingGroupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized MarketingGroupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingGroupsIdEndpoint: The initialized MarketingGroupsIdEndpoint object.
        """
        child = MarketingGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GroupModel]:
        """
        Performs a GET request against the /marketing/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GroupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            GroupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[GroupModel]:
        """
        Performs a GET request against the /marketing/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[GroupModel]: The parsed response data.
        """
        return self._parse_many(GroupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GroupModel:
        """
        Performs a POST request against the /marketing/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GroupModel: The parsed response data.
        """
        return self._parse_one(GroupModel, super().make_request("POST", params=params).json())
        