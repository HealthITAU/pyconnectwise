from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemLinksIdEndpoint import SystemLinksIdEndpoint
from pyconnectwise.endpoints.manage.SystemLinksCountEndpoint import SystemLinksCountEndpoint
from pyconnectwise.models.manage.LinkModel import LinkModel

class SystemLinksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "links", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLinksCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemLinksIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemLinksIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemLinksIdEndpoint: The initialized SystemLinksIdEndpoint object.
        """
        child = SystemLinksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LinkModel]:
        """
        Performs a GET request against the /system/links endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LinkModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LinkModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LinkModel]:
        """
        Performs a GET request against the /system/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LinkModel]: The parsed response data.
        """
        return self._parse_many(LinkModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LinkModel:
        """
        Performs a POST request against the /system/links endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LinkModel: The parsed response data.
        """
        return self._parse_one(LinkModel, super().make_request("POST", params=params).json())
        