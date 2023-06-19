from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyAccountIdDelegationsEndpoint import SystemMyAccountIdDelegationsEndpoint
from pyconnectwise.endpoints.manage.SystemMyAccountIdSkillsEndpoint import SystemMyAccountIdSkillsEndpoint
from pyconnectwise.models.manage.MyAccountModel import MyAccountModel

class SystemMyAccountIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.delegations = self.register_child_endpoint(
            SystemMyAccountIdDelegationsEndpoint(client, parent_endpoint=self)
        )
        self.skills = self.register_child_endpoint(
            SystemMyAccountIdSkillsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MyAccountModel]:
        """
        Performs a GET request against the /system/myAccount/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MyAccountModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MyAccountModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccountModel:
        """
        Performs a GET request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccountModel: The parsed response data.
        """
        return self._parse_one(MyAccountModel, super().make_request("GET", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccountModel:
        """
        Performs a PUT request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccountModel: The parsed response data.
        """
        return self._parse_one(MyAccountModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MyAccountModel:
        """
        Performs a PATCH request against the /system/myAccount/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MyAccountModel: The parsed response data.
        """
        return self._parse_one(MyAccountModel, super().make_request("PATCH", params=params).json())
        