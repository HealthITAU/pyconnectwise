from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesubcategoriesCountEndpoint import \
    ServiceKnowledgebasesubcategoriesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesubcategoriesIdEndpoint import \
    ServiceKnowledgebasesubcategoriesIdEndpoint
from pyconnectwise.models.manage import KnowledgeBaseSubCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceKnowledgebasesubcategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseSubCategories", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceKnowledgebasesubcategoriesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceKnowledgebasesubcategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasesubcategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgebasesubcategoriesIdEndpoint: The initialized ServiceKnowledgebasesubcategoriesIdEndpoint object.
        """
        child = ServiceKnowledgebasesubcategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[KnowledgeBaseSubCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseSubCategory]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseSubCategory, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseSubCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseSubCategory]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseSubCategory, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseSubCategory:
        """
        Performs a POST request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSubCategory: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSubCategory, super()._make_request("POST", data=data, params=params).json())
