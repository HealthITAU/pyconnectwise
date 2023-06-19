from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseArticlesIdEndpoint import ServiceKnowledgeBaseArticlesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseArticlesCountEndpoint import ServiceKnowledgeBaseArticlesCountEndpoint
from pyconnectwise.models.manage.KnowledgeBaseArticleModel import KnowledgeBaseArticleModel

class ServiceKnowledgeBaseArticlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseArticles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceKnowledgeBaseArticlesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceKnowledgeBaseArticlesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgeBaseArticlesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgeBaseArticlesIdEndpoint: The initialized ServiceKnowledgeBaseArticlesIdEndpoint object.
        """
        child = ServiceKnowledgeBaseArticlesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[KnowledgeBaseArticleModel]:
        """
        Performs a GET request against the /service/knowledgeBaseArticles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseArticleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            KnowledgeBaseArticleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseArticleModel]:
        """
        Performs a GET request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseArticleModel]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseArticleModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseArticleModel:
        """
        Performs a POST request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseArticleModel: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseArticleModel, super().make_request("POST", params=params).json())
        