from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsIdDownloadEndpoint import SystemDocumentsIdDownloadEndpoint
from pyconnectwise.endpoints.manage.SystemDocumentsIdThumbnailEndpoint import SystemDocumentsIdThumbnailEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPostable
from pyconnectwise.models.manage import DocumentInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemDocumentsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[DocumentInfo, ConnectWiseManageRequestParams],
    IPostable[DocumentInfo, ConnectWiseManageRequestParams],
    IPaginateable[DocumentInfo, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, DocumentInfo)
        IPostable.__init__(self, DocumentInfo)
        IPaginateable.__init__(self, DocumentInfo)

        self.download = self._register_child_endpoint(SystemDocumentsIdDownloadEndpoint(client, parent_endpoint=self))
        self.thumbnail = self._register_child_endpoint(SystemDocumentsIdThumbnailEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[DocumentInfo]:
        """
        Performs a GET request against the /system/documents/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DocumentInfo]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), DocumentInfo, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> DocumentInfo:
        """
        Performs a GET request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentInfo: The parsed response data.
        """
        return self._parse_one(DocumentInfo, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> DocumentInfo:
        """
        Performs a POST request against the /system/documents/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            DocumentInfo: The parsed response data.
        """
        return self._parse_one(DocumentInfo, super()._make_request("POST", data=data, params=params).json())
