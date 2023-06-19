from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemAuthAnvilsIdEndpoint import SystemAuthAnvilsIdEndpoint
from pyconnectwise.endpoints.manage.SystemAuthAnvilsCountEndpoint import SystemAuthAnvilsCountEndpoint
from pyconnectwise.endpoints.manage.SystemAuthAnvilsTestConnectionEndpoint import SystemAuthAnvilsTestConnectionEndpoint
from pyconnectwise.models.manage.AuthAnvilModel import AuthAnvilModel

class SystemAuthAnvilsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "authAnvils", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemAuthAnvilsCountEndpoint(client, parent_endpoint=self)
        )
        self.testConnection = self.register_child_endpoint(
            SystemAuthAnvilsTestConnectionEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemAuthAnvilsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemAuthAnvilsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemAuthAnvilsIdEndpoint: The initialized SystemAuthAnvilsIdEndpoint object.
        """
        child = SystemAuthAnvilsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AuthAnvilModel]:
        """
        Performs a GET request against the /system/authAnvils endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AuthAnvilModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AuthAnvilModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AuthAnvilModel]:
        """
        Performs a GET request against the /system/authAnvils endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AuthAnvilModel]: The parsed response data.
        """
        return self._parse_many(AuthAnvilModel, super().make_request("GET", params=params).json())
        