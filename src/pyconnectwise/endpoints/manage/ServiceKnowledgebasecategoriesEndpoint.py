from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasecategoriesCountEndpoint import (
    ServiceKnowledgebasecategoriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceKnowledgebasecategoriesIdEndpoint import (
    ServiceKnowledgebasecategoriesIdEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import KnowledgeBaseCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceKnowledgebasecategoriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[KnowledgeBaseCategory], ConnectWiseManageRequestParams],
    IPostable[KnowledgeBaseCategory, ConnectWiseManageRequestParams],
    IPaginateable[KnowledgeBaseCategory, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "knowledgeBaseCategories", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[KnowledgeBaseCategory])
        IPostable.__init__(self, KnowledgeBaseCategory)
        IPaginateable.__init__(self, KnowledgeBaseCategory)

        self.count = self._register_child_endpoint(
            ServiceKnowledgebasecategoriesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ServiceKnowledgebasecategoriesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasecategoriesIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServiceKnowledgebasecategoriesIdEndpoint: The initialized ServiceKnowledgebasecategoriesIdEndpoint object.
        """
        child = ServiceKnowledgebasecategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseCategory, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[KnowledgeBaseCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseCategory]: The parsed response data.
        """
        return self._parse_many(KnowledgeBaseCategory, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> KnowledgeBaseCategory:
        """
        Performs a POST request against the /service/knowledgeBaseCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseCategory: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseCategory, super()._make_request("POST", data=data, params=params).json())
