from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoAssignResourcesIdEndpoint import ServiceBoardsIdAutoAssignResourcesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoAssignResourcesCountEndpoint import ServiceBoardsIdAutoAssignResourcesCountEndpoint
from pyconnectwise.models.manage.BoardAutoAssignResourceModel import BoardAutoAssignResourceModel

class ServiceBoardsIdAutoAssignResourcesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "autoAssignResources", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdAutoAssignResourcesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdAutoAssignResourcesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdAutoAssignResourcesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdAutoAssignResourcesIdEndpoint: The initialized ServiceBoardsIdAutoAssignResourcesIdEndpoint object.
        """
        child = ServiceBoardsIdAutoAssignResourcesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardAutoAssignResourceModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/autoAssignResources endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardAutoAssignResourceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardAutoAssignResourceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardAutoAssignResourceModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/autoAssignResources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardAutoAssignResourceModel]: The parsed response data.
        """
        return self._parse_many(BoardAutoAssignResourceModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardAutoAssignResourceModel:
        """
        Performs a POST request against the /service/boards/{parentId}/autoAssignResources endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardAutoAssignResourceModel: The parsed response data.
        """
        return self._parse_one(BoardAutoAssignResourceModel, super().make_request("POST", params=params).json())
        