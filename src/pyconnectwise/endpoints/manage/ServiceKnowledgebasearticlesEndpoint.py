from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasearticlesCountEndpoint import \
    ServiceKnowledgebasearticlesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasearticlesIdEndpoint import ServiceKnowledgebasearticlesIdEndpoint
from pyconnectwise.models.manage import KnowledgeBaseArticle
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceKnowledgebasearticlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseArticles", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceKnowledgebasearticlesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceKnowledgebasearticlesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasearticlesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgebasearticlesIdEndpoint: The initialized ServiceKnowledgebasearticlesIdEndpoint object.
        """
        child = ServiceKnowledgebasearticlesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[KnowledgeBaseArticle]:
        """
        Performs a GET request against the /service/knowledgeBaseArticles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseArticle]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseArticle, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseArticle]:
        """
        Performs a GET request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseArticle]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseArticle, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseArticle:
        """
        Performs a POST request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseArticle: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseArticle, super()._make_request("POST", data=data, params=params).json())
