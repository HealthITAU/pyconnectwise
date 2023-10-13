from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechScriptFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScriptfoldersHierarchyEndpoint(
    ConnectWiseEndpoint, IGettable[list[LabTechScriptFolder], ConnectWiseAutomateRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "Hierarchy", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[LabTechScriptFolder])

    def get(
        self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None
    ) -> list[LabTechScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders/Hierarchy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechScriptFolder]: The parsed response data.
        """
        return self._parse_many(LabTechScriptFolder, super()._make_request("GET", data=data, params=params).json())
