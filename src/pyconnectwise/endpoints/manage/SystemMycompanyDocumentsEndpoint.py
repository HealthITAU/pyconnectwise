from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyDocumentsIdEndpoint import SystemMycompanyDocumentsIdEndpoint
from pyconnectwise.models.manage import DocumentSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyDocumentsEndpoint(ConnectWiseEndpoint):
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
        self, page: int, page_size: int, params: dict[str, int | str] = {}
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
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), DocumentSetup, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DocumentSetup]:
        """
        Performs a GET request against the /system/mycompany/documents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DocumentSetup]: The parsed response data.
        """
        return self._parse_many(DocumentSetup, super()._make_request("GET", data=data, params=params).json())
