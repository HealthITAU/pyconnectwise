from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SalesRolesIdEndpoint import SalesRolesIdEndpoint
from pyconnectwise.endpoints.manage.SalesRolesCountEndpoint import SalesRolesCountEndpoint
from pyconnectwise.models.manage.RoleModel import RoleModel

class SalesRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "roles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesRolesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SalesRolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesRolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesRolesIdEndpoint: The initialized SalesRolesIdEndpoint object.
        """
        child = SalesRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RoleModel]:
        """
        Performs a GET request against the /sales/roles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RoleModel]:
        """
        Performs a GET request against the /sales/roles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RoleModel]: The parsed response data.
        """
        return self._parse_many(RoleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RoleModel:
        """
        Performs a POST request against the /sales/roles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RoleModel: The parsed response data.
        """
        return self._parse_one(RoleModel, super().make_request("POST", params=params).json())
        