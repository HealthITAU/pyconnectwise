from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesubcategoriesCountEndpoint import (
    ServiceKnowledgebasesubcategoriesCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesubcategoriesIdEndpoint import (
    ServiceKnowledgebasesubcategoriesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import KnowledgeBaseSubCategory
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceKnowledgebasesubcategoriesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[KnowledgeBaseSubCategory], ConnectWiseManageRequestParams],
    IPostable[KnowledgeBaseSubCategory, ConnectWiseManageRequestParams],
    IPaginateable[KnowledgeBaseSubCategory, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "knowledgeBaseSubCategories", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[KnowledgeBaseSubCategory])
        IPostable.__init__(self, KnowledgeBaseSubCategory)
        IPaginateable.__init__(self, KnowledgeBaseSubCategory)

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
        child = ServiceKnowledgebasesubcategoriesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            KnowledgeBaseSubCategory,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[KnowledgeBaseSubCategory]:
        """
        Performs a GET request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[KnowledgeBaseSubCategory]: The parsed response data.
        """
        return self._parse_many(
            KnowledgeBaseSubCategory,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> KnowledgeBaseSubCategory:
        """
        Performs a POST request against the /service/knowledgeBaseSubCategories endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSubCategory: The parsed response data.
        """
        return self._parse_one(
            KnowledgeBaseSubCategory,
            super()._make_request("POST", data=data, params=params).json(),
        )
