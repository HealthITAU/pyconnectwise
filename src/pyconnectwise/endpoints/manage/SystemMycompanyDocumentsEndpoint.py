from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyDocumentsIdEndpoint import SystemMycompanyDocumentsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import DocumentSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMycompanyDocumentsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[DocumentSetup], ConnectWiseManageRequestParams],
    IPaginateable[DocumentSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> SystemMycompanyDocumentsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyDocumentsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyDocumentsIdEndpoint: The initialized SystemMycompanyDocumentsIdEndpoint object.
        """
        child = SystemMycompanyDocumentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[DocumentSetup]:
        """
        Performs a GET request against the /system/mycompany/documents endpoint and returns an initialized PaginatedResponse object.

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

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[DocumentSetup]:
        """
        Performs a GET request against the /system/mycompany/documents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DocumentSetup]: The parsed response data.
        """
        return self._parse_many(DocumentSetup, super()._make_request("GET", data=data, params=params).json())
