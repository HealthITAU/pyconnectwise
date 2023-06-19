from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.MarketingGroupsIdUsagesEndpoint import MarketingGroupsIdUsagesEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdCompaniesEndpoint import MarketingGroupsIdCompaniesEndpoint
from pyconnectwise.endpoints.manage.MarketingGroupsIdContactsEndpoint import MarketingGroupsIdContactsEndpoint
from pyconnectwise.models.manage.GroupModel import GroupModel

class MarketingGroupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.usages = self.register_child_endpoint(
            MarketingGroupsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.companies = self.register_child_endpoint(
            MarketingGroupsIdCompaniesEndpoint(client, parent_endpoint=self)
        )
        self.contacts = self.register_child_endpoint(
            MarketingGroupsIdContactsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[GroupModel]:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GroupModel:
        """
        Performs a GET request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GroupModel: The parsed response data.
        """
        return self._parse_one(GroupModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GroupModel:
        """
        Performs a PUT request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GroupModel: The parsed response data.
        """
        return self._parse_one(GroupModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GroupModel:
        """
        Performs a PATCH request against the /marketing/groups/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GroupModel: The parsed response data.
        """
        return self._parse_one(GroupModel, super().make_request("PATCH", params=params).json())
        