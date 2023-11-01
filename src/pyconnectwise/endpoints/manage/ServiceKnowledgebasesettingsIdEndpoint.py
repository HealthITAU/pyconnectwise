from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import KnowledgeBaseSettings
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceKnowledgebasesettingsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
    IPuttable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
    IPatchable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
    IPaginateable[KnowledgeBaseSettings, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, KnowledgeBaseSettings)
        IPuttable.__init__(self, KnowledgeBaseSettings)
        IPatchable.__init__(self, KnowledgeBaseSettings)
        IPaginateable.__init__(self, KnowledgeBaseSettings)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[KnowledgeBaseSettings]:
        """
        Performs a GET request against the /service/knowledgebasesettings/{id} endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            KnowledgeBaseSettings,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> KnowledgeBaseSettings:
        """
        Performs a GET request against the /service/knowledgebasesettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(
            KnowledgeBaseSettings,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> KnowledgeBaseSettings:
        """
        Performs a PUT request against the /service/knowledgebasesettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(
            KnowledgeBaseSettings,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> KnowledgeBaseSettings:
        """
        Performs a PATCH request against the /service/knowledgebasesettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            KnowledgeBaseSettings: The parsed response data.
        """
        return self._parse_one(
            KnowledgeBaseSettings,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
