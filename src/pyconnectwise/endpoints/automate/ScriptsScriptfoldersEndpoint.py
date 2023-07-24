from typing import Any

from pyconnectwise.endpoints.automate.ScriptsScriptfoldersIdEndpoint import ScriptsScriptfoldersIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.Scripts import SubmittableScriptFolder
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScriptsScriptfoldersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Scriptfolders", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> ScriptsScriptfoldersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ScriptsScriptfoldersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScriptsScriptfoldersIdEndpoint: The initialized ScriptsScriptfoldersIdEndpoint object.
        """
        child = ScriptsScriptfoldersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SubmittableScriptFolder:
        """
        Performs a POST request against the /Scripts/Scriptfolders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SubmittableScriptFolder: The parsed response data.
        """
        return self._parse_one(SubmittableScriptFolder, super()._make_request("POST", data=data, params=params).json())
