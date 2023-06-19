from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeWorkRolesIdEndpoint import TimeWorkRolesIdEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesCountEndpoint import TimeWorkRolesCountEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesInfoEndpoint import TimeWorkRolesInfoEndpoint
from pyconnectwise.models.manage.WorkRoleModel import WorkRoleModel

class TimeWorkRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkRolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeWorkRolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeWorkRolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorkRolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeWorkRolesIdEndpoint: The initialized TimeWorkRolesIdEndpoint object.
        """
        child = TimeWorkRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkRoleModel]:
        """
        Performs a GET request against the /time/workRoles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkRoleModel]:
        """
        Performs a GET request against the /time/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleModel]: The parsed response data.
        """
        return self._parse_many(WorkRoleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleModel:
        """
        Performs a POST request against the /time/workRoles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleModel: The parsed response data.
        """
        return self._parse_one(WorkRoleModel, super().make_request("POST", params=params).json())
        