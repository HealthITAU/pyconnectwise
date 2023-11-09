from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemGoogleemailsetupIdTestconnectionEndpoint import (
    SystemGoogleemailsetupIdTestconnectionEndpoint,
)
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import GoogleEmailSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SystemGoogleemailsetupIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[GoogleEmailSetup, ConnectWiseManageRequestParams],
    IPatchable[GoogleEmailSetup, ConnectWiseManageRequestParams],
    IPuttable[GoogleEmailSetup, ConnectWiseManageRequestParams],
    IPaginateable[GoogleEmailSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, GoogleEmailSetup)
        IPatchable.__init__(self, GoogleEmailSetup)
        IPuttable.__init__(self, GoogleEmailSetup)
        IPaginateable.__init__(self, GoogleEmailSetup)

        self.test_connection = self._register_child_endpoint(
            SystemGoogleemailsetupIdTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[GoogleEmailSetup]:
        """
        Performs a GET request against the /system/googleemailsetup/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[GoogleEmailSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), GoogleEmailSetup, self, page, page_size, params
        )

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /system/googleemailsetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> GoogleEmailSetup:
        """
        Performs a GET request against the /system/googleemailsetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GoogleEmailSetup: The parsed response data.
        """
        return self._parse_one(GoogleEmailSetup, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> GoogleEmailSetup:
        """
        Performs a PATCH request against the /system/googleemailsetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GoogleEmailSetup: The parsed response data.
        """
        return self._parse_one(GoogleEmailSetup, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> GoogleEmailSetup:
        """
        Performs a PUT request against the /system/googleemailsetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GoogleEmailSetup: The parsed response data.
        """
        return self._parse_one(GoogleEmailSetup, super()._make_request("PUT", data=data, params=params).json())
