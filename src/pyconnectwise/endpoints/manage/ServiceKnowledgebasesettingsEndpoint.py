from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceKnowledgebasesettingsIdEndpoint import ServiceKnowledgebasesettingsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import KnowledgeBaseSettings
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceKnowledgebasesettingsEndpoint(
    ConnectWiseEndpoint,
    IGettable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
    IPostable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
    IPaginateable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "knowledgebasesettings", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, KnowledgeBaseSettings)
        IPostable.__init__(self, KnowledgeBaseSettings)
        IPaginateable.__init__(self, KnowledgeBaseSettings)

    def id(self, id: int) -> ServiceKnowledgebasesettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceKnowledgebasesettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceKnowledgebasesettingsIdEndpoint: The initialized ServiceKnowledgebasesettingsIdEndpoint object.
        """
        child = ServiceKnowledgebasesettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[KnowledgeBaseSettings]:
        """
        Performs a GET request against the /service/knowledgebasesettings endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[KnowledgeBaseSettings]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), KnowledgeBaseSettings, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> KnowledgeBaseSettings:
        """
        Performs a GET request against the /service/knowledgebasesettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSettings, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> KnowledgeBaseSettings:
        """
        Performs a POST request against the /service/knowledgebasesettings endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(KnowledgeBaseSettings, super()._make_request("POST", data=data, params=params).json())
