from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.TimeWorkRolesIdInfoEndpoint import TimeWorkRolesIdInfoEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesIdUsagesEndpoint import TimeWorkRolesIdUsagesEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesIdLocationsEndpoint import TimeWorkRolesIdLocationsEndpoint
from pyconnectwise.models.manage.WorkRoleModel import WorkRoleModel

class TimeWorkRolesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.info = self.register_child_endpoint(
            TimeWorkRolesIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            TimeWorkRolesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            TimeWorkRolesIdLocationsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkRoleModel]:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint and returns an initialized PaginatedResponse object.

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
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleModel:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleModel: The parsed response data.
        """
        return self._parse_one(WorkRoleModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleModel:
        """
        Performs a PUT request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleModel: The parsed response data.
        """
        return self._parse_one(WorkRoleModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkRoleModel:
        """
        Performs a PATCH request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRoleModel: The parsed response data.
        """
        return self._parse_one(WorkRoleModel, super().make_request("PATCH", params=params).json())
        