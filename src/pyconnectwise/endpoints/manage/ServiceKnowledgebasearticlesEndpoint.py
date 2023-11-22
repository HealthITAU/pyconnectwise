from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasearticlesCountEndpoint import (
    ServiceKnowledgebasearticlesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceKnowledgebasearticlesIdEndpoint import ServiceKnowledgebasearticlesIdEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import KnowledgeBaseArticle
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceKnowledgebasearticlesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[KnowledgeBaseArticle], ConnectWiseManageRequestParams],
    IPostable[KnowledgeBaseArticle, ConnectWiseManageRequestParams],
    IPaginateable[KnowledgeBaseArticle, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "knowledgeBaseArticles", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[KnowledgeBaseArticle])
        IPostable.__init__(self, KnowledgeBaseArticle)
        IPaginateable.__init__(self, KnowledgeBaseArticle)

        self.count = self._register_child_endpoint(
            ServiceKnowledgebasearticlesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ServiceKnowledgebasearticlesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasearticlesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServiceKnowledgebasearticlesIdEndpoint: The initialized ServiceKnowledgebasearticlesIdEndpoint object.
        """
        child = ServiceKnowledgebasearticlesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseArticle, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[KnowledgeBaseArticle]:
        """
        Performs a GET request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseArticle]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseArticle, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> KnowledgeBaseArticle:
        """
        Performs a POST request against the /service/knowledgeBaseArticles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseArticle: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseArticle, super()._make_request("POST", data=data, params=params).json())
