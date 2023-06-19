from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoTemplatesIdEndpoint import ServiceBoardsIdAutoTemplatesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdAutoTemplatesCountEndpoint import ServiceBoardsIdAutoTemplatesCountEndpoint
from pyconnectwise.models.manage.BoardAutoTemplateModel import BoardAutoTemplateModel

class ServiceBoardsIdAutoTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "autoTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdAutoTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceBoardsIdAutoTemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceBoardsIdAutoTemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceBoardsIdAutoTemplatesIdEndpoint: The initialized ServiceBoardsIdAutoTemplatesIdEndpoint object.
        """
        child = ServiceBoardsIdAutoTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[BoardAutoTemplateModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/autoTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardAutoTemplateModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            BoardAutoTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[BoardAutoTemplateModel]:
        """
        Performs a GET request against the /service/boards/{parentId}/autoTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[BoardAutoTemplateModel]: The parsed response data.
        """
        return self._parse_many(BoardAutoTemplateModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BoardAutoTemplateModel:
        """
        Performs a POST request against the /service/boards/{parentId}/autoTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardAutoTemplateModel: The parsed response data.
        """
        return self._parse_one(BoardAutoTemplateModel, super().make_request("POST", params=params).json())
        