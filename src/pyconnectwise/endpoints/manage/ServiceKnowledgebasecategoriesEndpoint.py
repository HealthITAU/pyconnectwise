from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasecategoriesCountEndpoint import \
    ServiceKnowledgebasecategoriesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasecategoriesIdEndpoint import \
    ServiceKnowledgebasecategoriesIdEndpoint
from pyconnectwise.models.manage import KnowledgeBaseCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ServiceKnowledgebasecategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "knowledgeBaseCategories", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            ServiceKnowledgebasecategoriesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceKnowledgebasecategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasecategoriesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgebasecategoriesIdEndpoint: The initialized ServiceKnowledgebasecategoriesIdEndpoint object.
        """
        child = ServiceKnowledgebasecategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[KnowledgeBaseCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseCategories endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseCategory]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseCategory, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[KnowledgeBaseCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseCategory]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseCategory, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> KnowledgeBaseCategory:
        """
        Performs a POST request against the /service/knowledgeBaseCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseCategory: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseCategory, super()._make_request("POST", data=data, params=params).json())
