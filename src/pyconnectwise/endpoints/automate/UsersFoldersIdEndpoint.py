from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
)
from pyconnectwise.models.automate import AutomateUserFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    PatchRequestData,
)


class UsersFoldersIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[AutomateUserFolder, ConnectWiseAutomateRequestParams],
    IPatchable[AutomateUserFolder, ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateUserFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, AutomateUserFolder)
        IPatchable.__init__(self, AutomateUserFolder)
        IPaginateable.__init__(self, AutomateUserFolder)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateUserFolder]:
        """
        Performs a GET request against the /Users/Folders/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateUserFolder]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateUserFolder,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateUserFolder:
        """
        Performs a GET request against the /Users/Folders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUserFolder: The parsed response data.
        """
        return self._parse_one(
            AutomateUserFolder,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /Users/Folders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> AutomateUserFolder:
        """
        Performs a PATCH request against the /Users/Folders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateUserFolder: The parsed response data.
        """
        return self._parse_one(
            AutomateUserFolder,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
