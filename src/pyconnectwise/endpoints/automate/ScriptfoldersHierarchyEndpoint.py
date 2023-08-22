from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechScriptFolder
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptfoldersHierarchyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Hierarchy", parent_endpoint=parent_endpoint)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[LabTechScriptFolder]:
        """
        Performs a GET request against the /Scriptfolders/Hierarchy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechScriptFolder]: The parsed response data.
        """
        return self._parse_many(LabTechScriptFolder, super()._make_request("GET", data=data, params=params).json())
