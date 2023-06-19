from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesIdEndpoint import ServiceKnowledgeBaseSubCategoriesIdEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesCountEndpoint import ServiceKnowledgeBaseSubCategoriesCountEndpoint
from pyconnectwise.models.manage.KnowledgeBaseSubCategoryModel import KnowledgeBaseSubCategoryModel

class ServiceKnowledgeBaseSubCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseSubCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceKnowledgeBaseSubCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ServiceKnowledgeBaseSubCategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgeBaseSubCategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgeBaseSubCategoriesIdEndpoint: The initialized ServiceKnowledgeBaseSubCategoriesIdEndpoint object.
        """
        child = ServiceKnowledgeBaseSubCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[KnowledgeBaseSubCategoryModel]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseSubCategoryModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            KnowledgeBaseSubCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseSubCategoryModel]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseSubCategoryModel]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseSubCategoryModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseSubCategoryModel:
        """
        Performs a POST request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSubCategoryModel: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSubCategoryModel, super().make_request("POST", params=params).json())
        