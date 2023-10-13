from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import DocumentSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMycompanyDocumentsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[DocumentSetup, ConnectWiseManageRequestParams],
    IPuttable[DocumentSetup, ConnectWiseManageRequestParams],
    IPatchable[DocumentSetup, ConnectWiseManageRequestParams],
    IPaginateable[DocumentSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, DocumentSetup)
        IPuttable.__init__(self, DocumentSetup)
        IPatchable.__init__(self, DocumentSetup)
        IPaginateable.__init__(self, DocumentSetup)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[DocumentSetup]:
        """
        Performs a GET request against the /system/mycompany/documents/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DocumentSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), DocumentSetup, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> DocumentSetup:
        """
        Performs a GET request against the /system/mycompany/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentSetup: The parsed response data.
        """
        return self._parse_one(DocumentSetup, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> DocumentSetup:
        """
        Performs a PUT request against the /system/mycompany/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentSetup: The parsed response data.
        """
        return self._parse_one(DocumentSetup, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> DocumentSetup:
        """
        Performs a PATCH request against the /system/mycompany/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentSetup: The parsed response data.
        """
        return self._parse_one(DocumentSetup, super()._make_request("PATCH", data=data, params=params).json())
