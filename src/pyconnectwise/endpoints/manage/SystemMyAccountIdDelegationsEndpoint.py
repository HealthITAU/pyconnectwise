from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyAccountIdDelegationsIdEndpoint import SystemMyAccountIdDelegationsIdEndpoint
from pyconnectwise.endpoints.manage.SystemMyAccountIdDelegationsCountEndpoint import SystemMyAccountIdDelegationsCountEndpoint
from pyconnectwise.models.manage.MemberDelegationModel import MemberDelegationModel

class SystemMyAccountIdDelegationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "delegations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyAccountIdDelegationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyAccountIdDelegationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyAccountIdDelegationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyAccountIdDelegationsIdEndpoint: The initialized SystemMyAccountIdDelegationsIdEndpoint object.
        """
        child = SystemMyAccountIdDelegationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberDelegationModel]:
        """
        Performs a GET request against the /system/myAccount/{parentId}/delegations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberDelegationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberDelegationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberDelegationModel]:
        """
        Performs a GET request against the /system/myAccount/{parentId}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberDelegationModel]: The parsed response data.
        """
        return self._parse_many(MemberDelegationModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberDelegationModel:
        """
        Performs a POST request against the /system/myAccount/{parentId}/delegations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberDelegationModel: The parsed response data.
        """
        return self._parse_one(MemberDelegationModel, super().make_request("POST", params=params).json())
        