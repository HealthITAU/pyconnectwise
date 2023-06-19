from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeWorkRolesIdLocationsIdEndpoint import TimeWorkRolesIdLocationsIdEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesIdLocationsCountEndpoint import TimeWorkRolesIdLocationsCountEndpoint
from pyconnectwise.models.manage.WorkRoleLocationModel import WorkRoleLocationModel

class TimeWorkRolesIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkRolesIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> TimeWorkRolesIdLocationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized TimeWorkRolesIdLocationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeWorkRolesIdLocationsIdEndpoint: The initialized TimeWorkRolesIdLocationsIdEndpoint object.
        """
        child = TimeWorkRolesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkRoleLocationModel]:
        """
        Performs a GET request against the /time/workRoles/{parentId}/locations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRoleLocationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkRoleLocationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WorkRoleLocationModel]:
        """
        Performs a GET request against the /time/workRoles/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkRoleLocationModel]: The parsed response data.
        """
        return self._parse_many(WorkRoleLocationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleLocationModel:
        """
        Performs a POST request against the /time/workRoles/{parentId}/locations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleLocationModel: The parsed response data.
        """
        return self._parse_one(WorkRoleLocationModel, super().make_request("POST", params=params).json())
        