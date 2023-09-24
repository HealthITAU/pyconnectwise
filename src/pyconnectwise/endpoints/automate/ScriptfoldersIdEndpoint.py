from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechScriptFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScriptfoldersIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechScriptFolder, ConnectWiseAutomateRequestParams],
    IPatchable[LabTechScriptFolder, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechScriptFolder, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechScriptFolder]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechScriptFolder, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechScriptFolder:
        """
        Performs a GET request against the /Scriptfolders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechScriptFolder: The parsed response data.
        """
        return self._parse_one(LabTechScriptFolder, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /Scriptfolders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def patch(
        self, data: PatchRequestData, params: ConnectWiseAutomateRequestParams | None = None
    ) -> LabTechScriptFolder:
        """
        Performs a PATCH request against the /Scriptfolders/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechScriptFolder: The parsed response data.
        """
        return self._parse_one(LabTechScriptFolder, super()._make_request("PATCH", data=data, params=params).json())
