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
from pyconnectwise.models.manage import GLCaption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceGlcaptionsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[GLCaption, ConnectWiseManageRequestParams],
    IPuttable[GLCaption, ConnectWiseManageRequestParams],
    IPatchable[GLCaption, ConnectWiseManageRequestParams],
    IPaginateable[GLCaption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, GLCaption)
        IPuttable.__init__(self, GLCaption)
        IPatchable.__init__(self, GLCaption)
        IPaginateable.__init__(self, GLCaption)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[GLCaption]:
        """
        Performs a GET request against the /finance/glCaptions/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GLCaption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            GLCaption,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> GLCaption:
        """
        Performs a GET request against the /finance/glCaptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLCaption: The parsed response data.
        """
        return self._parse_one(
            GLCaption, super()._make_request("GET", data=data, params=params).json()
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> GLCaption:
        """
        Performs a PUT request against the /finance/glCaptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLCaption: The parsed response data.
        """
        return self._parse_one(
            GLCaption, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> GLCaption:
        """
        Performs a PATCH request against the /finance/glCaptions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GLCaption: The parsed response data.
        """
        return self._parse_one(
            GLCaption, super()._make_request("PATCH", data=data, params=params).json()
        )
