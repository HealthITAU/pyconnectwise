from typing import Any

from pyconnectwise.endpoints.automate.ScriptsIdEndpoint import ScriptsIdEndpoint
from pyconnectwise.endpoints.automate.ScriptsScriptfoldersEndpoint import ScriptsScriptfoldersEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import AutomateScript
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Scripts", parent_endpoint=parent_endpoint)

        self.scriptfolders = self._register_child_endpoint(ScriptsScriptfoldersEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ScriptsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScriptsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScriptsIdEndpoint: The initialized ScriptsIdEndpoint object.
        """
        child = ScriptsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AutomateScript:
        """
        Performs a POST request against the /Scripts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AutomateScript: The parsed response data.
        """
        return self._parse_one(AutomateScript, super()._make_request("POST", data=data, params=params).json())
