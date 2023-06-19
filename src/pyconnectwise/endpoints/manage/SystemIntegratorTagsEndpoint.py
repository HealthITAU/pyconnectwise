from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemIntegratorTagsIdEndpoint import SystemIntegratorTagsIdEndpoint
from pyconnectwise.endpoints.manage.SystemIntegratorTagsCountEndpoint import SystemIntegratorTagsCountEndpoint
from pyconnectwise.models.manage.IntegratorTagModel import IntegratorTagModel

class SystemIntegratorTagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "integratorTags", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemIntegratorTagsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemIntegratorTagsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemIntegratorTagsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemIntegratorTagsIdEndpoint: The initialized SystemIntegratorTagsIdEndpoint object.
        """
        child = SystemIntegratorTagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[IntegratorTagModel]:
        """
        Performs a GET request against the /system/integratorTags endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[IntegratorTagModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            IntegratorTagModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[IntegratorTagModel]:
        """
        Performs a GET request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[IntegratorTagModel]: The parsed response data.
        """
        return self._parse_many(IntegratorTagModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> IntegratorTagModel:
        """
        Performs a POST request against the /system/integratorTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IntegratorTagModel: The parsed response data.
        """
        return self._parse_one(IntegratorTagModel, super().make_request("POST", params=params).json())
        